#!/usr/bin/python3
# Copyright (C) 2024 Dez Moleski dez@moleski.com
# MIT License: All uses allowed with attribution.
#
from wordgames import Word, WordList, AnagramsDict, LetterSetBitmask, ALPHABET_LIST
import sys
from copy import deepcopy
from glob import glob
import datetime
import json
import os.path

def sorted_letters(s: set) -> str:
   l = list(s)
   l.sort()
   return ''.join(l)


def sorted_words_str(words: list, mutable: bool) -> str:
   '''Words is a list of strings. Mutable tells us if we must copy before sorting.'''
   # Put the given list into a canonical form that we can
   # use to recognize whether it's just a permutation of a
   # list that we've already seen.
   if not mutable:
      mutable_list = words.copy() # We're not allowed to modify the given list!
   else:
      mutable_list = words
   mutable_list.sort()
   return ' '.join(mutable_list)


KNOWN_PGRAMS = set()
def is_new_pangram(pgram: list, mutable: bool) -> str:
   '''Returns canonical pangram string if this is a new pangram, None if already known'''
   
   canon_str = sorted_words_str(pgram, mutable)
   
   if canon_str in KNOWN_PGRAMS:
      return None
   else:
      KNOWN_PGRAMS.add(canon_str)
      return canon_str

if __name__ == "__main__":
   if len(sys.argv) != 1:
      exit("Usage: pangram-counts")
   
   # Read ALL GUESSES file
   ALL_FILE = "./ALL"
   print("Reading all valid guesses file:", ALL_FILE, file=sys.stderr, flush=True, end=' ')
   valid_guesses = WordList.from_file(ALL_FILE)
   valid_guesses.sort()
   print("N =", len(valid_guesses), file=sys.stderr, flush=True)
   
   # Read ANSWERS
   ANSWERS_FILE = "./ANSWERS"
   print("Reading answers file:", ANSWERS_FILE, file=sys.stderr, flush=True, end=' ')
   answers = WordList.from_file(ANSWERS_FILE)
   answers.sort()
   print("N =", len(answers), file=sys.stderr, flush=True)
   
   # Visit each pangram data file
   print("Scanning data files: ", file=sys.stderr, flush=True, end='')
   all_pgrams = list()
   all_words = WordList()
   answers_used = WordList()
   total_pangrams = 0
   for letter in ALPHABET_LIST:
      print(letter, file=sys.stderr, flush=True, end=' ')
      datadir = f"./data/{letter}/"
      if os.path.isdir(datadir):
         # Visit each file in the data dir
         paths = sorted(glob(datadir+'*'))
         for filepath in paths:
            with open(filepath, 'r') as f:
               # Read each line and split first into line_list array.
               # Anagrams within the line are like: '[VIGOR|VIRGO]'
               # Ignore lines that start with '#'
               for line in f:
                  line_list = line.split()
                  if line_list[0] != '#':
                     all_pgrams.append(line_list) # unexpanded anagrams here
                     # Visit each word or anagram set in the line, and
                     # accumulate the words into our all_words WordList.
                     # Also count how many pangrams are generated by expanding any anagrams.
                     count_this_pangram = 1
                     for item in line_list:
                        # If it's five letters, this item is a single word
                        if len(item) == 5:
                           all_words.add_str(item)
                           if answers.contains(item):
                              answers_used.add_str(item)
                        else:
                           # It's anagrams like '[VIGOR|VIRGO]', so trim and split it into words.
                           stripped = item.strip('[]')
                           words = stripped.split('|')
                           count_this_pangram *= len(words)
                           for w in words:
                              all_words.add_str(w)
                              if answers.contains(w):
                                 answers_used.add_str(item)
                     total_pangrams += count_this_pangram
   print('', file=sys.stderr, flush=True)
   
   print("N base pangrams:", len(all_pgrams), file=sys.stderr, flush=True)
   print("N expanded pangrams:", total_pangrams, file=sys.stderr, flush=True)
   percent = len(all_words) / len(valid_guesses)
   print(f"N words used: {len(all_words)} / {len(valid_guesses)} = {percent:.0%}", file=sys.stderr, flush=True)
   percent = len(answers_used) / len(answers)
   print(f"N answers used: {len(answers_used)} / {len(answers)} = {percent:.0%}", file=sys.stderr, flush=True)
   