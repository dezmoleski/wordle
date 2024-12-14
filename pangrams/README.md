### Wordle Pangrams
Copyright (C) 2024 Dez Moleski dez@moleski.com

#### See also:
- https://rentry.co/wordle-meta-list
- https://rentry.co/W5W25L742

#### Other pangram-related articles:
- https://en.wikipedia.org/wiki/Pangram
- https://medium.com/@FallingForFallacies/all-perfect-pangrams-of-english-8c8d0f621bee

### Definitions
- **Anagram**: A rearrangement of the letters of a word or phrase, yielding another.
- **Heterogram**: A word or phrase with no repeated letters.
- **Pangram**: A phrase or set of words containing all letters of some alphabet (A-Z for us).
- **Perfect anagram**: A rearrangement of the letters of a word or phrase, yielding another, using the same number of repeated letters as the original.
- **Perfect pangram**: A phrase or set of words containing all letters of some alphabet EXACTLY once each.

"Anagram" is most often used to mean "perfect anagram."  In my code and discussion "anagram" means: "formed from the same set of letters without regard to repeats" which may also be called an imperfect anagram.

The word "set" is herein used exclusively in the formal sense, where each element in a set is distinct by definition: no element can be repeated in a set.

For example: `AALII` and `ILIAL` are both formed from the letter set `{A,I,L}` and are therefore anagrams of each other. But they are certainly imperfect anagrams, since `AALII` repeats the `A` while `ILIAL` repeats the `L`.

Similarly, perfect pangrams contain each letter of the target alphabet exactly once, while regular pangrams contain all the alphabet letters, but some may be repeated: "The quick brown fox jumps over the lazy dog" is 35 letters, with several repeated. "Mr Jock, TV quiz PhD, bags few lynx" is a perfect pangram over A-Z in English, albeit with use of abbreviations.

In any further discussion the "imperfect" qualifier is implicit.

### Known Wordleable Pangrams

#### Pangrams Generated from 25-letter Heterograms
One way to find pangrams that can be played in Wordle is to combine one of the twenty-five known five-word, twenty-five letter Wordleable heterograms (abbreviated "h-grams" below) listed at https://rentry.co/W5W25L742 with a Wordleable word containing the twenty-sixth letter that transforms that heterogram into a pangram.

##### Winning Wordle With a Pangram
This leads to what is probably the best way to play a pangram in Wordle and still win the game without knowing the answer in advance. The first instance of this known to the author was recorded in this play by @WT: https://nyti.ms/3Hf10eR#permid=130444396 that used the one "missing G" h-gram `CROMB JIVED KLUTZ PHYNX WAQFS` on Wordle `0939 DOING` to complete the pangram win (on the seventh day of trying: some luck required!).

@WT devised a clever method to increase the odds of winning with a pangram by playing the three words first that are in common with an h-gram that omits `V`: `CROMB`, `WAQFS` and `PHYNX`. `V` gives the second-best chance to get a pangram play, appearing in 148 Solutions (6%) compared to `G` which appears in 299 Solutions (13%). See https://rentry.co/wordle-letter-freq for more details about letter frequencies in Wordle Solutions.

After playing `CROMB`, `WAQFS` and `PHYNX`, you must commit to guessing whether the Solution for that day contains a `G` or a `V`. If you think the Solution contains a `V` you continue with `GLITZ` and `JUKED`. If you think the Solution contains a `G` then continue with `JIVED` and `KLUTZ`. (And if you are sure the solution contains neither `G` nor `V` you might as well solve it as quickly as you can: you're not getting a pangram win on that day!)

@WT's method increases the odds of winning with a pangram from a 13% chance each day (neglecting the effect of previously-used Solutions aka PU/PS) to nearly a 19% chance (taking into account the 15 Solutions that contain both a `G` and a `V`). Pretty good odds, and 100% effective for a skilled and patient player such as @WT is!

In fact, I've simplified @WT's actual method above: they were also thinking about a possible `J` solution using the heterogram `CROMB GIVED KLUTZ PHYNX WAQFS` which shares `KLUTZ` with the missing-`G` h-gram. So if you play `CROMB`, `WAQFS`, `PHYNX`, and `KLUTZ` you still keep the possibility of solving with a pangram if the answer contains a `J` by playing `GIVED` fifth instead of `JIVED`. This ups the daily odds by another percent to about a 20% chance per day that you attempt to win with a pangram.

The decision tree during play looks like this:

```text
Step 1:  \\ 

Step 2:   | - play CROMB, WAQFS, PHYNX in any order you prefer
Step 3:	 /

At this point (or earlier) if you're sure the solution doesn't contain G, J, or V
you should solve it and try again another day. But if you think it might contain
one of those letters, then continue with the decisions shown inside [..] below.

       [Decide: Do you think the solution contains a V?]
            |                                    |
          G or J (No V)                        Yes V
            |                                    |
Step 4: Play KLUTZ                           Play GLITZ or JUKED (i.e. commit to V path or solve).
            |                                Then on step 5 play the other one, or solve if the
   [Does the solution contain a J?]          solution doesn't turn out to contain a V.
            |                   |
          G (No J)           Yes J 
            |                   |
Step 5: Play JIVED          Play GIVED
          or solve (if solution doesn't contain G or J)

Step 6: Solve and collect your pangram win, or hope for better luck tomorrow!
```

Finally, if you do win Wordle with a pangram by any method, be sure to get a screen capture of your completed game showing ALL the letters of the keyboard have changed color. This is half the fun of winning with a pangram, so save that screen capture to share later with other Wordle players.

**Known Pangram Wins:**
1. Wordle `0939 DOING` - https://nyti.ms/3Hf10eR#permid=130444396 @WT
1. Wordle `0944 THING` - https://nyti.ms/3U0EDkS#permid=130556623 @Wordler
1. Wordle `0995 GRASP` - https://nyti.ms/49Gjwt0#permid=131749118 @Dez
1. Wordle `1023 VOILA` - the first V!
    + https://www.nytimes.com/shared/comment/3u7o0b @Couchpumpkin
    + @Couchpumpkin went on a 10 day quest for a V-pangram with DRECK GLITZ JUMBO PHYNX WAQFS, eschewing the algorithm given above and quoting Hemingway while fishing patiently and confidently.

##### Total Number of Pangrams Generated from Heterograms
There is:
- 1 h-gram missing the letter `G`
  + Combined with 1,748 Wordleable words containing `G` for 1,748 possible pangrams

There are:
- 8 h-grams missing the letter `J`
  + Combined with 340 Wordleable words containing `J` for 2,720 possible pangrams
- 5 h-grams missing the letter `Q`
  + Combined with 143 Wordleable words containing `Q` for 715 possible pangrams
- 5 h-grams missing the letter `V`
  + Combined with 773 Wordleable words containing `V` for 3,865 possible pangrams
- 6 h-grams missing the letter `X`
  + Combined with 325 Wordleable words containing `X` for 1,950 possible pangrams

For a total of (1,748 + 2,720 + 715 + 3,865 + 1,950) = **10,998 Wordleable pangrams** that can be generated from the known h-grams.

#### Pangrams Found by Exhaustive Search

See https://tinyurl.com/5n8s2kam

The first implementation of the exhaustive search in Python was agonizingly slow and would have required years, possibly decades, of runtime on my current laptop to complete the search. 

I have implemented a basic version of the exhaustive search in C that already runs about 60 times faster than the Python searcher. This program does not yet include optimizations based on previous work with heterograms.

Results and code are published under the MIT License, available via the URL above.

An unsuccessful attempt to solve a random archive game using the intermediate data and GNU/Linux command line tools can be seen here: https://rentry.co/wordle-manual-pangram-example


##### Status
**Updated 13 Dec 2024** (views 1335)

The search program has been running on up to twelve computers, but several have gone idle, waiting for improved distributed search management code.

Currently ~8 productive instances of the search are running, covering a little over 1% of the search area remaining per week.

- D-Z are complete (representing ~17% of the search space).
- A, B, and C are in progress.
- Searches from 843 of 2149 head words starting with A (360/718), B (149/710), or C (334/721) are complete.
- About 50.7% of the total search space has been covered to date.

##### Counts
- 16,241,610 "base" pangrams (without expanding anagrams) have been found. 
- 27,041,965 total pangrams (with anagrams expanded) have been found.
- 19,929,769 pangrams (74%) contain at least one known potential solution.
- 12,912 of 14,855 valid guesses (87%) appear in pangrams found to date.
- 2,096 of 2,319 known potential solutions (90%) appear in pangrams found to date.

The following 105 known potential solutions (4.5%) have not been found in any pangrams yet, and yielded no pangrams when the search started from that word (which is more consequential for words earlier in the alphabet than later, due to the basic search optimization of proceeding only with lexically-greater words from the head word).
~~~text
ABASE ABBEY ABUSE ARISE AROSE
ASSAY ASSET AUDIO
BASIS
CACAO COCOA
DADDY DAISY DIODE
EARLY EASEL EERIE ENNUI ENSUE
ERROR ESSAY ETUDE
HAIRY HARRY HARSH HELLO HILLY
HORSE HOUSE HURRY HUSSY
ISSUE
KAYAK
LAYER LEASE LEASH LEERY LOOSE
LORRY LOSER LOUSE LOUSY
MAMMA MAMMY MOMMY MUMMY
NANNY NINNY NOISE NOOSE
ONION
PAUSE PAYEE PIOUS POISE POPPY
POSSE PUPPY
RAISE RELAY REUSE RISER ROUSE
ROYAL RULER RURAL
SALSA SASSY SAUTE SEEDY SENSE
SEPIA SHALE SHALL SHARE SHEAR
SHEER SHELL SHIRE SHORE SHUSH
SILLY SISSY SLASH SLYLY SOLAR
SOOTY SORRY STATE STEAD STEED
STOUT SUITE SULLY SURER SUSHI
TASTE TASTY TATTY TEASE TESTY
TOAST
UNION USHER
YEAST
~~~

Top 25 words occurring in pangrams found to date. The list shows the percent (and number) of pangrams found to date that contain each word:
1. `VOZHD` : 28% (7607806) 
1. `WAQFS` : 24% (6524089) 
1. `VIBEX` : 12% (3369015) 
1. `PHYNX` : 10% (2821756) 
1. `JUMBY` : 9% (2485298) 
1. `QUAWK` : 8% (2286319) 
1. `QUICK` : 6% (1653687) 
1. `QUACK` : 6% (1604162) 
1. `QUECK` : 5% (1384981) 
1. `FIQHS` : 5% (1360200) 
1. `FJELD` : 5% (1336701) 
1. `FJORD` : 5% (1336351) 
1. `VEXED` : 4% (1114943) 
1. `JAMBS` : 4% (1061773) 
1. `QUBIT` : 4% (970340) 
1. `JUMPY` : 3% (945559) 
1. `GLITZ` : 3% (905763) 
1. `JUDGY` : 3% (893445) 
1. `JOCKY` : 3% (891837) 
1. `JIVED` : 3% (865528) 
1. `SQUIZ` : 3% (854584) 
1. `FRITZ` : 3% (839674) 
1. `PHLOX` : 3% (836471) 
1. `JIMPY` : 3% (829845) 
1. `JACKY` : 3% (778098) 


#### Pangrams Comprised of Solutions Only
See https://rentry.co/wordle-pangrams-solutions-only

### Pangram-related posts in the NYT Wordle Review Comments:
- 02024 Jan 01 - https://nyti.ms/3NM3dSH#permid=130151139
- 02024 Jan 13 - https://nyti.ms/3Sk0OkR#permid=130437156
- 02024 Feb 10 - https://nyti.ms/3wjHrj0#permid=131087126
- 02024 Feb 23 - https://nyti.ms/3uBhZW3#permid=131367700
- 02024 Feb 28 - https://nyti.ms/3Tf3C2U#permid=131484206
- 02024 Mar 07 - https://nyti.ms/433r4nj#permid=131685392
- 02024 Mar 17 - https://www.nytimes.com/shared/comment/3tpkj5
- 02024 Mar 19 - https://www.nytimes.com/shared/comment/3tqus9
- 02024 Mar 29 - https://www.nytimes.com/shared/comment/3u27j7
- 02024 Sep 14 - https://www.nytimes.com/shared/comment/41scvq
- 02024 Dec 14 - https://www.nytimes.com/shared/comment/43s620
