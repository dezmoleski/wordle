#!/usr/bin/python3
#
from wordgames import Word, WordList, AnagramsDict, LetterSetBitmask
import sys
from copy import deepcopy
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
   if len(sys.argv) != 3:
      exit("Usage: check-pangrams word-list pangrams-list")
   
   # The given word list file should contain all 5L words desired to search
   # to validate the pangrams from the pangrams list file.
   ALL_WORDS_FILE = sys.argv[1]
   print("Reading word list:", ALL_WORDS_FILE, file=sys.stderr, flush=True)
   all_words = WordList.from_file(ALL_WORDS_FILE)
   all_words.sort()
   
   # We can prune all but one of any sets of anagrammatic words.
   # Any pangrams found for one anagram work with all anagrams.
   anagrams_dict = AnagramsDict()
   anagrams_dict.add_wordlist(all_words)
   anagrams_dict.prune() # Remove entries with just one anagram, i.e. the root word
   anagrams_dict.sort() # Sort the lists of anagrams within the dict for consistent results
   
   # We're done with initial setup, print a couple things to make
   # rough timing of the setup steps easy.
   print("All words len:", len(all_words), file=sys.stderr, flush=True)
   print("Anagrams dict entries:", len(anagrams_dict), file=sys.stderr, flush=True)
   print("Anagrams total count:", anagrams_dict.total_words(), file=sys.stderr, flush=True)
   
   # TODO: not sure if this is useful yet
   alphabet_set = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

   # Read through the pangrams file. Just echo lines that don't split into six elements.
   # Any line with six elements should be a pangram, but if it fails the pangram test
   # we're just going to echo it with a leading '!' so it's obvious for later pruning.
   #
   # Read any lines already in the OUTPUT_FILE to look for
   # a list of words to skip ahead to. Any line with six words
   # in the WORD_LIST_FILE at the end of it is considered to
   # mean this run should skip ahead to those words (presumably
   # to resume where the last run left off, got it?).
   PANGRAM_LIST_FILE = sys.argv[2]
   pgrams_list = list()
   if os.path.isfile(PANGRAM_LIST_FILE):
      with open(PANGRAM_LIST_FILE, 'r') as f:
         for line in f:
            line_list = line.split()
            if len(line_list) != 6:
               print(line, end='')
            else:
               # OK, we have a line of six strings separated by whitespace.
               all_six_are_words = True
               letter_set = set()
               for w in line_list:
                  # Check that the next string is in the word list.
                  if not all_words.contains(w):
                     print("!WORD NOT FOUND:", w, file=sys.stderr, flush=True)
                     all_six_are_words = False
                     break
                  else:
                     # Accumulate the letters of w into the letter-set for this line.
                     letter_set.update(set(w))
                     
               if all_six_are_words:
                  # All six strings are words in the all_words list.
                  # Check to see if the alleged pangram actually uses all 26 letters.
                  if letter_set != alphabet_set:
                     print("!NOT A PANGRAM:", line, end='', file=sys.stderr, flush=True)
                  else:
                     # Validate pangram is not a duplicate and print if not.
                     pgram_str = is_new_pangram(line_list, mutable=False)
                     if not pgram_str is None:
                        print(line, end='')
                        pgrams_list.append(pgram_str)
                     else:
                        print("!DUPLICATE:", line, end='', file=sys.stderr, flush=True)
               else:
                  print("!SOME WORDS NOT FOUND:", line, end='', file=sys.stderr, flush=True)
   
   # PRINT OUT PANGRAMS WITH ANAGRAMS!
   # pgrams_list at this point contains all the found solutions,
   # as strings of space-separated words in canonical (sorted) order.
   #
   # But any word in any of those pangram lists might have anagrams.
   #
   print('------------------------------------------------------------')
   
   n_total = 0
   for canon_str in pgrams_list:
      n_this_gram = 1
      pgram_strs = canon_str.split()
      for word_str in pgram_strs:
         word_anagrams = anagrams_dict.anagrams_of_str(word_str)
         if word_anagrams is None:
            print(word_str, end=' ')
         else:
            print(f'[{word_str}', end='')
            for w in word_anagrams:
               print(f'|{w}', end='')
            print("]", end=' ')
            n_this_gram *= (1+len(word_anagrams))
      print('')
      n_total += n_this_gram
   print("Total pangrams counting anagrams:", n_total, file=sys.stderr, flush=True)
