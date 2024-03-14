#!/usr/bin/python3
#
# Copyright (C) 2024 Dez Moleski dez@moleski.com
# MIT License: All uses allowed with attribution.
#

from wordgames import Word, WordList, AnagramsDict, LetterSetBitmask
import sys
import os.path
from copy import deepcopy

if __name__ == "__main__":
    # The given word list file should contain all 5L words desired to search
    # to validate the pangrams from the pangrams list file.
    ALL_WORDS_FILE = "ALL"
    print("Reading word list:", ALL_WORDS_FILE, file=sys.stderr, flush=True)
    all_words = WordList.from_file(ALL_WORDS_FILE)
    all_words.sort()

    # Build a helper dict with the word as the key, and the word index
    # as the value. For the C Wordle word lists, we offset the "natural"
    # C index by one, so that word index zero can be used as the "null"
    # word. So the first word has index one.
    word2index = dict()
    index: int = 1
    for w in all_words.word_list:
        word2index[w.word] = index
        index += 1
    
    # We can prune all but one of any sets of anagrammatic words.
    # Any pangrams found for one anagram work with all anagrams.
    # JUST REMEMBER TO CHECK FOR ANAGRAMS AT THE END TO PRINT
    # THOSE OUT AS PART OF THE FINAL RESULTS! THEY COUNT AS
    # DISTINCT SOLUTIONS even if we don't need to waste time
    # representing them as separate nodes in the search space.
    anagrams_dict = AnagramsDict()
    anagrams_dict.add_wordlist(all_words)
    anagrams_dict.prune() # Remove entries with just one anagram, i.e. the root word
    anagrams_dict.sort() # Sort the lists of anagrams within the dict for consistent results

    """
    # Find and print the longest list of anagrams
    longest: int = 0
    long_k = None
    long_v = None
    for k,v in anagrams_dict.anagrams.items():
        if len(v) > longest:
            longest = len(v)
            long_k = k
            long_v = v
    print("Most anagrams: n=", longest, "k=", long_k, "v=", long_v, file=sys.stderr, flush=True)
    """
    
    # Start with a copy of all the given words.
    # Then remove all but the first anagram listed for each entry in the anagrams dict.
    # The resulting list contains no anagrams of any of the words in the list.
    no_anagrams = deepcopy(all_words)
    for agrams in anagrams_dict.anagrams.values():
        for wordstr in agrams[1:]:
            no_anagrams.remove_str(wordstr)
    no_anagrams.sort()
    
    OUT_FILE = "all_words.inl"
    if os.path.isfile(OUT_FILE):
        exit("File exists: " + OUT_FILE)

    with open(OUT_FILE, 'w') as outf:
        print('#include "wordle.h"\n', file=outf)
        print(f'#define N_WORDS {len(all_words)}\n', file=outf)
        print('WordleWord ALL_WORDS[N_WORDS+1] = {\n  {}, // used as a flag value for the NULL word or no-word WORD_NUM==0', file=outf)
        i: int = 0
        for w in all_words.word_list:
            i += 1
            print(f'  /* {i} */ {{"{w.word}"', end='', file=outf)
            print(f',"{w.sorted_letters()}"', end='', file=outf)
            print(f',{w.letter_set_mask}', end='', file=outf)
            print(f',{len(w.letter_set)}', end='', file=outf)
            print('},', file=outf)
        print('};', file=outf)
        
        print('', file=outf)

        print(f'#define N_ANAGRAMS {len(anagrams_dict)}\n', file=outf)
        print('WordleAnagram ANAGRAMS[N_ANAGRAMS+1] = {\n  {}, // used as a flag to indicate the NULL anagram or no-anagrams', file=outf)
        keys = sorted(anagrams_dict.anagrams.keys())
        for k in keys:
            v = anagrams_dict.anagrams[k]
            print(f'  {{"{k}"', end='', file=outf)
            print(f',{len(v)}', end='', file=outf)
            print(',{', end='', file=outf)
            lastw = v[-1]
            for wd in v:
                print(word2index[wd], end='', file=outf)
                if wd != lastw:
                    print(',', end='', file=outf)
            print('}},', file=outf)
        print('};', file=outf)
        
        print('', file=outf)
        
        print(f'#define N_NO_ANAGRAMS {len(no_anagrams)}\n', file=outf)
        print('uint16_t NO_ANAGRAMS[N_NO_ANAGRAMS] = {', file=outf)
        for w in no_anagrams.word_list:
            print(f'  {word2index[w.word]}, // {w.word}', file=outf)
        print('};', file=outf)
        
       
   
