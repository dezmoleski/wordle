#!/usr/bin/python3
# Copyright (C) 2024 Dez Moleski dez@moleski.com
# MIT License: All uses allowed with attribution.
#
from wordgames import Word, WordList, AnagramsDict, LetterSetBitmask, ALPHABET_LIST
import sys
from copy import deepcopy
from glob import glob
from operator import itemgetter
from itertools import islice
import datetime
import json
import os.path
import re

import cmd

# Suggested: use a generator when reading large files
def lines(filepath):
   with open(filepath, 'r') as f:
      for line in f:
         yield line.rstrip()

def increment_word_count(d: dict, w: str):
   d[w] = d.get(w, 0) + 1

def list_top_counts(d: dict, N: int):
   # Sort the (k,v) tuples in the given dict by value, highest to lowest, and slice off the top N
   l = sorted(d.items(), key=itemgetter(1), reverse=True)
   return l[0:N]

# This WORDS dictionary speeds things up by not re-constructing
# instances of the Word class over and over again.
WORDS = dict()
def get_word(word_str: str):
   word = WORDS.get(word_str, None)
   if word is None:
      word = Word(word_str)
      WORDS[word_str] = word
   return word

class PangramShell(cmd.Cmd):
   intro = 'Welcome to the Wordle pangrams shell.  Type help or ? to list commands.\n'
   prompt = 'pangram> '
   
   ALL_FILE = "./ALL"
   ANSWERS_FILE = "./ANSWERS"
   ALL_PANGRAMS = './SOLUTION-PANGRAMS'
   valid_guesses = None
   answers  = None

   # These data members are reset by clear()
   played_words: list = None
   pangrams: list = None
   letters_left: set = None
   letters_left_list: list = None
   
   ##
   ## BASE CLASS OVERRIDES
   ##
   def __init__(self):
      super().__init__()
      # Read ALL SOLUTIONS (ANSWERS) file
      print("Reading answers file:", self.ANSWERS_FILE, "...", end=' ', flush=True)
      self.answers = WordList.from_file(self.ANSWERS_FILE)
      self.answers.sort()
      # Load solution words into the local WORDS cache, indexed both by 'WORD' and 'WORD*'
      for w in self.answers.word_list:
         w.star()
         WORDS[w.word] = w
         WORDS[w.word+'*'] = w
      print("N =", len(self.answers), flush=True)
      
      # Read ALL GUESSES file
      print("Reading all valid guesses file:", self.ALL_FILE, "...", end=' ', flush=True)
      self.valid_guesses = WordList.from_file(self.ALL_FILE)
      self.valid_guesses.sort()
      # Load non-solution words into the local WORDS cache, indexed only by 'WORD'
      for w in self.valid_guesses.word_list:
         if not w.word in WORDS:
            WORDS[w.word] = w
      print("N =", len(self.valid_guesses), flush=True)
      self.clear()
      
   def postcmd(self, stop, line):
      return line == 'bye' or line == 'exit' or line == 'quit'

   ##
   ## HELPER MEMBER FUNCTIONS
   ##
   def clear(self):
      self.played_words = list()
      self.pangrams = list() # pangrams available to play
      self.letters_left = set(ALPHABET_LIST)
      self.letters_left_list = ALPHABET_LIST
      
   def n_played(self):
      return len(self.played_words)

   def pangrams_remaining(self):
      """ Return count of the remaining pangrams """
      if len(self.played_words) > 0:
         return len(self.pangrams)
      return 37421839

   def played(self, w):
      return w.word in [x.word for x in self.played_words]

   ##
   ## DO_something members
   ##
   def do_bye(self, arg):
      """ Say bye (exit the program) """
      print("Byeee!")
      
   def do_exit(self, arg):
      """ Exit the program """
      print("Exiting...")
      
   def do_quit(self, arg):
      """ Quit the program """
      print("Quitting...")

   def do_clear(self, arg):
      self.clear()
      self.do_status(None)
      
   def do_common(self, arg):
      """ Find the most common unplayed words in the remaining pangrams, or:
      if given up to 5 words as arguments, find the most common unplayed words in pangrams with those words (excluding those words).
      Scanning for common unplayed words only proceeds when the number of pangrams to scan is 3 million or fewer.
      """
      given_words = None
      if len(arg) > 0:
         temp_words = list()
         gw_list = arg.split()
         if len(gw_list) > 5:
            print(f'At most 5 words can be searched for common unplayed words.')
            return # PUNCH-OUT
         for gw in gw_list:
            given_word = get_word(gw)
            if not self.valid_guesses.contains_word(given_word):
               print(f'{given_word} is not Wordleable.')
               return # PUNCH-OUT
            temp_words.append(given_word)
         n_to_scan = 0
         for p in self.pangrams:
            for w in temp_words:
               if w.word in p:
                  n_to_scan += 1
         given_words = temp_words
      else:
         n_to_scan = self.pangrams_remaining()
      
      if n_to_scan > 10000000:
         print(f'{n_to_scan} is too many pangrams to scan: "common" requires fewer than 10 million to scan.')
      else:
         inner_loop_count = 0
         skip_words_list = [x.word for x in self.played_words]

         if given_words is None:
            print('Finding top 10 common unplayed words in pangrams remaining', flush=True)
         else:
            print(f'Finding top 10 common unplayed words in pangrams with {given_words}', flush=True)
            skip_words_list.extend([x.word for x in given_words])
            
         if given_words is None:
            counts = dict()
            for p in self.pangrams:
               words_list = p.split()
               for word_str in words_list:
                  inner_loop_count += 1
                  if inner_loop_count % 200000 == 0:
                     print('.', end='', flush=True)
                  w = get_word(word_str)
                  # Ignore words we already played plus the given word, if any
                  if not w.word in skip_words_list:
                     increment_word_count(counts, w.word)
            print('', flush=True)
            # Sort the k,v pairs of the counts dict by the values and get the top 10
            l = list_top_counts(counts, 10) # list of tuples k,v
            for t in l:
               print(t[0], t[1])
         else:
            common_counts = None
            common_counts_min = None
            for given_word in given_words:
               print(f'=== {given_word.word}', end='', flush=True)
               counts = dict()
               for p in self.pangrams:
                  if given_word.word in p:
                     words_list = p.split()
                     for word_str in words_list:
                        inner_loop_count += 1
                        if inner_loop_count % 200000 == 0:
                           print('.', end='', flush=True)
                        w = get_word(word_str)
                        # Ignore words we already played plus the given word, if any
                        if not w.word in skip_words_list:
                           increment_word_count(counts, w.word)
               print('', flush=True)
               # Sort the k,v pairs of the counts dict by the values and print the top 10
               l = list_top_counts(counts, 10) # list of tuples k,v
               for t in l:
                  print(t[0], t[1])
               # If we're past the first iteration, find the intersection of the counts dicts.
               if common_counts is None:
                  common_counts = counts
               else:
                  intersect_keys = common_counts.keys() & counts.keys()
                  new_common_counts = {key: max(common_counts[key],counts[key]) for key in intersect_keys}
                  common_counts_min = {key: min(common_counts[key],counts[key]) for key in intersect_keys}
                  common_counts = new_common_counts
            if len(given_words) > 1:
               print(f'====== COMMON max counts')
               # Sort the k,v pairs of the counts dict by the values and print the top 10
               l = list_top_counts(common_counts, 10) # list of tuples k,v
               for t in l:
                  print(t[0], t[1])
               print(f'====== COMMON min counts')
               # Sort the k,v pairs of the counts dict by the values and print the top 10
               l = list_top_counts(common_counts_min, 10) # list of tuples k,v
               for t in l:
                  print(t[0], t[1])
   
   def do_echo(self, arg):
      """ Just echo the args """
      print(f'arg = "{arg}"', f'Type of arg is {type(arg)}')

   TOP_LIST = [
      ('WAQFS', 9812605, 2063),
      ('VOZHD', 9173872, 1906),
      ('PHYNX', 3391283, 1756),
      ('QUAWK', 3325194, 1946),
      ('VIBEX', 3322065, 1982),
      ('FJORD', 2872084, 1631),
      ('JUMPY', 2845176, 1778),
      ('QUICK', 2792910, 1638),
      ('QUACK', 2719095, 1687),
      ('JUMBY', 2122386, 1715),
      ('FIQHS', 1911577, 1402),
      ('FJELD', 1904839, 1497),
      ('VEXED', 1612513, 1611),
      ('FRITZ', 1594095, 1205),
      ('JIMPY', 1580090, 1715),
      ('JIVED', 1556037, 1689),
      ('JUDGY', 1470095, 1723),
      ('QUECK', 1453228, 1648),
      ('SQUIZ', 1360372, 1423),
      ('WALTZ', 1230223, 1262),
      ('BLITZ', 1186288, 1291),
      ('VIXEN', 1157491, 1485),
      ('GLITZ', 1075438, 1586),
      ('BLONX', 1040214, 1670),
      ('JOCKY', 953657, 1757),
      ('QOPHS', 947182, 1205),
      ('JAMBS', 946046, 1532),
      ('JUMBO', 933604, 1495),
      ('VITEX', 915549, 1336),
      ('VOXEL', 896269, 1289),
      ('BUXOM', 845828, 1542),
      ('GUQIN', 840115, 1388),
      ('PHLOX', 835688, 1355),
      ('JACKY', 835383, 1666),
      ('QUBIT', 804713, 1131),
      ('QAPIK', 800603, 1380),
      ('BORTZ', 771645, 1231),
      ('KLUTZ', 764054, 1432),
      ('VEXIL', 739236, 1275),
      ('JUMPS', 710609, 1440),
      ('GLYPH', 661088, 1000),
      ('BOXTY', 631444, 1397),
      ('ZIMBS', 613198, 1407),
      ('ZYGON', 599747, 1241),
      ('BANTZ', 597463, 1294),
      ('PYXED', 590059, 1036),
      ('PLOTZ', 588892, 1200),
      ('CEZVE', 575685, 1508),
      ('FLAXY', 554593, 1187),
      ('ZINGY', 521973, 1235),
   ]
   """
   TOP_LIST = [
      ('WAQFS',9812605),
      ('VOZHD',9173872),
      ('PHYNX',3391283),
      ('QUAWK',3325194),
      ('VIBEX',3322065),
      ('FJORD',2872084),
      ('JUMPY',2845176),
      ('QUICK',2792910),
      ('QUACK',2719095),
      ('JUMBY',2122386),
      ('FIQHS',1911577),
      ('FJELD',1904839),
      ('VEXED',1612513),
      ('FRITZ',1594095),
      ('JIMPY',1580090),
      ('JIVED',1556037),
      ('JUDGY',1470095),
      ('QUECK',1453228),
      ('SQUIZ',1360372),
      ('WALTZ',1230223),
      ('BLITZ',1186288),
      ('VIXEN',1157491),
      ('GLITZ',1075438),
      ('BLONX',1040214),
      ('JOCKY',953657),
      ('QOPHS',947182),
      ('JAMBS',946046),
      ('JUMBO',933604),
      ('VITEX',915549),
      ('VOXEL',896269),
      ('BUXOM',845828),
      ('GUQIN',840115),
      ('PHLOX',835688),
      ('JACKY',835383),
      ('QUBIT',804713),
      ('QAPIK',800603),
      ('BORTZ',771645),
      ('KLUTZ',764054),
      ('VEXIL',739236),
      ('JUMPS',710609),
      ('GLYPH',661088),
      ('BOXTY',631444),
      ('ZIMBS',613198),
      ('ZYGON',599747),
      ('BANTZ',597463),
      ('PYXED',590059),
      ('PLOTZ',588892),
      ('CEZVE',575685),
      ('FLAXY',554593),
      ('ZINGY',521973)
   ]
   """
   
   def count_solutions(self, word: str):
      answers_left = set()
      for p in self.pangrams:
         words_list = p.split()
         for word_str in words_list:
            w = get_word(word_str)
            if w.starred:
               answers_left.add(w.word)
      return len(answers_left)

   def do_genlist(self, arg):
      """ GENERATE the list of words found in most pangrams, and how many unique solutions each one leaves if played first """
      print('Word ', ' Pangrams', ' Solutions')
      print('-----', ' --------', ' ---------')
      for (w,n,_) in self.TOP_LIST:
         #print(w, f'{n:8d}')
         print(f"('{w}',", n, end=', ', flush=True)
         self.clear()
         for line in lines(self.ALL_PANGRAMS):
            if w in line:
               self.pangrams.append(line)
         n_solutions = self.count_solutions(w)
         print(f'{n_solutions}),', flush=True)
      self.clear()
      
   def do_list(self, arg):
      """ Print the list of words found in most pangrams, and how many unique solutions each one leaves if played first """
      print('Word ', ' Pangrams', ' Solutions')
      print('-----', ' --------', ' ---------')
      l = sorted(self.TOP_LIST, key=itemgetter(2), reverse=True)
      for (w,n,s) in l:
         print(w, f'{n:8d}     {s}')
      
   def play_word(self, w):
      """ Play a word """
      # Words given to be played must be in the ALL list, of course.
      if not self.valid_guesses.contains_word(w):
         print(f'{w} is not Wordleable.')
      elif self.played(w):
         print(f'You already played {w}!')
      else:
         if self.n_played() == 0: # This is the first word played
            # Load each line of the ALL-PANGRAMS file that contains the first word.
            first_word = w.word
            n_lines = 0
            print(f"Scanning {self.ALL_PANGRAMS} for {first_word}", flush=True, end='')
            for line in lines(self.ALL_PANGRAMS):
               n_lines += 1
               if n_lines % 1000000 == 0:
                  print('.', flush=True, end='')
               if first_word in line:
                  self.pangrams.append(line)
            print('')
         else:
            next_word = w.word
            next_pangrams = list()
            for p in self.pangrams:
               if next_word in p:
                  next_pangrams.append(p)
            self.pangrams = next_pangrams
         
         self.played_words.append(w)
         self.letters_left -= w.letter_set
         self.letters_left_list = list(self.letters_left)
         self.letters_left_list.sort()

   def do_play(self, arg):
      """ Play one or more given words """
      for word_str in arg.split():
         self.play_word(get_word(word_str))
      self.do_status(None)
         
   def do_print(self, arg):
      """ With no argument, print all the remaining pangrams if 100 or fewer remain.
      Given a word as an argument, print up to 100 remaining pangrams containing that word.
      """
      pangrams_remaining = self.pangrams_remaining()
      if len(arg) == 0 and pangrams_remaining > 100:
         print(f'There are {pangrams_remaining} pangrams remaining. Print only prints when 100 or fewer remain.')
      else:
         word = None
         if len(arg) > 0:
            w = get_word(arg.split()[0])
            if self.valid_guesses.contains_word(w):
               word = w
            else:
               print(f'{w} is not Wordleable.')
               return # PUNCH-OUT
         n_printed = 0
         for p in self.pangrams:
            if word is None or word.word in p:
               print(p)
               n_printed += 1
               if n_printed == 100:
                  return # PUNCH-OUT
   
   def do_solutions(self, arg):
      """ Get info about solutions in the remaining pangrams.
      A regular expression pattern can optionally be given.
      For example .L... matches only solutions with L in slot 2,
      or .*O.* matches solutions containing an O anywhere.
      If the number of [matching] solutions is <= 200, they are printed.
      """
      pattern = None
      if len(arg) > 0:
         try:
            pattern = re.compile(arg.upper())
         except:
            print(f'ERROR: pattern {arg} failed to compile as a regular expression.', flush=True)
            pattern = None
            
      pangrams_remaining = self.pangrams_remaining()
      if pangrams_remaining > 10000000:
         print(f'{pangrams_remaining} pangrams remaining is too many to get solution info.')
      else:
         answers_left = set()
         inner_loop_count = 0
         print('Counting solutions', end='', flush=True)
         for p in self.pangrams:
            words_list = p.split()
            for word_str in words_list:
               inner_loop_count += 1
               if inner_loop_count % 200000 == 0:
                  print('.', end='', flush=True)
               w = get_word(word_str)
               if w.starred:
                  if pattern is None or pattern.fullmatch(w.word):
                     answers_left.add(w)
         print('')
         if pattern is None:
            print(f'{len(answers_left)} unique solutions are in the remaining pangrams.')
         else:
            print(f'{len(answers_left)} unique solutions matching {arg} are in the remaining pangrams.')
         
         if len(answers_left) <= 200:
            l = list(answers_left)
            l.sort()
            n_printed = 0
            for w in l:
               n_printed += 1
               print(w.word, end=' ' if n_printed % 10 > 0 else '\n')
            print('')
            
   def do_status(self, arg):
      """ Print current status info """
      pangrams_remaining = self.pangrams_remaining()
      print(f'There are {pangrams_remaining} pangrams remaining.')
      print('Played:', self.played_words)
      print(f'{len(self.letters_left_list)} letters unplayed:', end=' ')
      for l in self.letters_left_list:
         print(l, end=' ')
      print('')
      
   def do_think(self, arg):
      """ Think about a word """
      w = get_word(arg)
      # Words given to be thought about must be in the ALL list, of course.
      if not self.valid_guesses.contains_word(w):
         print(f'{w} is not Wordleable.')
      else:
         if self.answers.contains_word(w):
            print(f'{w} is a known potential solution.')
         if self.n_played() == 0:
            print('Play at least one word to get more information.')
         else:
            if self.played(w):
               print(f'You already played {w}!')
            else:
               n_pangrams = 0
               for p in self.pangrams:
                  if w.word in p:
                     n_pangrams += 1
               print(f'{w} is in {n_pangrams} of the remaining pangrams.')
         
if __name__ == "__main__":
   if len(sys.argv) != 1:
      exit("Usage: play-pangram")

   """
   # Read ANSWERS

   # Read PU
   PU_FILE = "./PU"
   print("Reading PU file:", PU_FILE, file=sys.stderr, flush=True, end=' ')
   pu = WordList.from_file(PU_FILE)
   pu.sort()
   print("N =", len(pu), file=sys.stderr, flush=True)

   # Derive NU from ANSWERS - PU
   print("Deriving NU from {ANSWERS - PU}:", file=sys.stderr, flush=True, end=' ')
   nu_set = answers.word_set - pu.word_set
   nu = WordList.from_word_set(nu_set)
   nu.sort()
   print("N =", len(nu), file=sys.stderr, flush=True)
   """

   """
   /*
         # Split first into line_list array.
         line_list = line.split()
         pangram = list()
         for item in line_list:
            word = Word(item)
            pangram.append(word)
   */
   """
   
   PangramShell().cmdloop()
   
