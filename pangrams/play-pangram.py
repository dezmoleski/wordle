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

class PangramShell(cmd.Cmd):
   intro = 'Welcome to the Wordle pangrams shell.  Type help or ? to list commands.\n'
   prompt = 'pangram> '
   
   played_words = list()
   last_played_word = None
   ALL_FILE = "./ALL"
   ANSWERS_FILE = "./ANSWERS"
   ALL_PANGRAMS = './SOLUTION-PANGRAMS'
   valid_guesses = None
   pangrams = list() # pangrams available to play
   answers  = None
   letters_left = set(ALPHABET_LIST)
   letters_left_list = ALPHABET_LIST
   
   ##
   ## BASE CLASS OVERRIDES
   ##
   def __init__(self):
      super().__init__()
      # Read ALL GUESSES file
      print("Reading all valid guesses file:", self.ALL_FILE, "...", end=' ')
      self.valid_guesses = WordList.from_file(self.ALL_FILE)
      self.valid_guesses.sort()
      print("N =", len(self.valid_guesses))
      print("Reading answers file:", self.ANSWERS_FILE, "...", end=' ')
      self.answers = WordList.from_file(self.ANSWERS_FILE)
      self.answers.sort()
      print("N =", len(self.answers))
      
   def postcmd(self, stop, line):
      return line == 'bye'

   ##
   ## HELPER MEMBER FUNCTIONS
   ##
   def n_played(self):
      return len(self.played_words)

   def pangrams_remaining(self):
      """ Return count of the remaining pangrams """
      if len(self.played_words) > 0:
         return len(self.pangrams)
      return 54470144

   def played(self, w):
      return w.word in [x.word for x in self.played_words]
   
   ##
   ## DO_something members
   ##
   def do_bye(self, arg):
      """ Exit the program """
      print("Byeee!")
      
   def do_echo(self, arg):
      """ Just echo the args """
      print(f'arg = "{arg}"', f'Type of arg is {type(arg)}')

   def do_play(self, arg):
      """ Play a word """
      w = Word(arg)
      # Words given to be played must be in the ALL list, of course.
      if not self.valid_guesses.contains_word(w):
         print(f'{w} is not Wordleable.')
      elif self.played(w):
         print(f'You already played {w}!')
      else:
         if self.last_played_word is None: # This is the first word played
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
            n_pangrams = 0
            # Just count how many pangrams we have that contain the next word
            next_pangrams = list()
            for p in self.pangrams:
               if next_word in p:
                  n_pangrams += 1
                  next_pangrams.append(p)
            self.pangrams = next_pangrams
         
         self.last_played_word = w
         self.played_words.append(w)
         self.letters_left -= w.letter_set
         self.letters_left_list = list(self.letters_left)
         self.letters_left_list.sort()
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
            w = Word(arg.split()[0])
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
      """ Get info about solutions in the remaining pangrams """
      # Think about qualifying by a given word too: w = Word(arg)
      pangrams_remaining = self.pangrams_remaining()
      if pangrams_remaining > 5000000:
         print(f'{pangrams_remaining} pangrams remaining is too many to get solution info.')
      else:
         answers_left = set()
         inner_loop_count = 0
         print('Counting solutions', end='', flush=True)
         for p in self.pangrams:
            words_list = p.split()
            for word_str in words_list:
               inner_loop_count += 1
               if inner_loop_count % 10000 == 0:
                  print('.', end='', flush=True)
               w = Word(word_str)
               if w.starred:
                  answers_left.add(w)
         print('')
         print(f'{len(answers_left)} unique solutions are in the remaining pangrams.')
         if len(answers_left) < 200:
            l = list(answers_left)
            l.sort()
            for w in l:
               print(w.word, end=' ')
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
      w = Word(arg)
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
   
