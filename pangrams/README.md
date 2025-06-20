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
**Updated 19 June 2025** (views 1740)

**Fast Pruning Algorithm**

My son found an amazing optimization of the search by pruning dead ends using a cleverly constructed cache of search state whenever a dead end is discovered. This enables the entire search to run in a single instance of the search program within about an hour on my main laptop! He also wrote his version of the search from scratch, AND ran it in parallel on a GPU, further reducing the run time to just a few minutes. **So proud of him!** and yet humbled that I never thought of these optimizations.

**Double and Triple Checking**

Because the slower searcher was so close to finishing its run though, I let it run to completion. But I also added my own implementation of the fast pruning to make a third version of the searcher. Upon checking the slow searcher results against both my and my son's implementation of the new fast-pruner, none of the 3 result sets matched!

However, the difference between my and my son's fast pruners was easy to diagnose as a simple off-by-one error in his version (score one for the old man!) and apart from that they agreed to 99.999989% (6 pangrams missing out of 54.47 million). The slow searcher is a different story...

**Slow Searcher History and Results**

The final slow search program was run on up to twelve computers, with multiple instances per computer, but I let several of the slowest go idle, thinking I might write improved distributed search management code to reduce the manual tending that took up to an hour each day. But I hit an equilibrium and a pace of progress I could live with (about 1 hour overhead per week and 2% progress) and never did write the fancy search management system.

The earliest version of the slow searcher was written in python, which clearly had some relatively significant flaws (or else the all-too-human operator of that program made mistakes). I think it was bugs in the code though, based on details I won't go into here.

Bottom line is I'm re-running the portion of the search that didn't match the fast pruners, which was in the range of K-P only (i.e. the search results starting from A through J, and Q through Z all matched the fast pruners' results). This will provide a final check that the fast pruner was not TOO aggressive in its pruning of the search space, and should be done in another few days. I don't think this is going to find further errors (famous last words) because the remaining discrepancies are all pangrams missing from the slow searcher results. I believe the only over-aggressive pruning happened back in the oldest slow python searcher.

Finally, my post-processing scripts that provide the counts below are mostly dependent on the data format used by the slow searcher, which is just different enough from the fast pruners' output that I haven't re-written them (yet) to work from the better data provided by the fast pruners. Just another reason to get the slow-search data to match results from the fast-pruners.

##### Counts
These are a combination of results from the slow searchers and the fast pruners, **NOT final**.

- 32,349,989 "base" pangrams (without expanding anagrams) have been found. 
  + **PROBABLY SLIGHTLY UNDER FINAL COUNT**
- 54,470,144 total pangrams (with anagrams expanded) have been found. 
  + **FAST PRUNER CORRECTED TOTAL**
- **INCORRECT OVERCOUNT so fewer than:** 40,575,749 pangrams (75%) contain at least one known potential solution.
  + The (**closer to-**)corrected count via a double-checking program is 37,416,787 (69% of total pangrams)
- 13,862 of 14,855 valid guesses (93%) appear in pangrams found to date. 
  + **BASED ON INCOMPLETE SLOW SEARCH DATA**
- 2,224 of 2,325 known potential solutions (95.66%) appear in pangrams found to date. 
  + **BASED ON INCOMPLETE SLOW SEARCH DATA**

The following 101 known potential solutions (4.34%) are not found in any pangrams. 
  + **BASED ON INCOMPLETE SLOW SEARCH DATA**
~~~text
ABASE ABBEY ABUSE AISLE ALLAY
ALLEY ALLOY AMASS AMISS ANNOY
ARISE AROSE ARRAY ASIDE ASSAY
ASSET AUDIO
BASIS BAYOU BOBBY BOOBY
CACAO COCOA
DADDY DAISY DIODE
EARLY EASEL EERIE ENNUI ENSUE
ERASE ERROR ESSAY
HOUSE HUSSY
INANE ISSUE
LASER LASSO LAYER LEASE LEERY
LOOSE LORRY LOSER LOUSE LOUSY
LOYAL
MAMMA MAMMY
NANNY NINNY NOISE NOOSE
OBESE ONION
PAUSE PIOUS POISE POPPY POSSE
PUPPY
RAISE RALLY RARER RELAY REUSE
RISER ROUSE ROYAL RULER RURAL
SALLY SALSA SASSY SAUNA SAUTE
SEEDY SENSE SEPIA SHUSH SILLY
SISSY SLYLY SOLAR SOOTY SORRY
STATE STOUT SUEDE SULLY SURER
SUSHI
TASTE TASTY TATTY TEASE TOAST
UNION USUAL
~~~

Top 25 words occurring in pangrams containing solutions found to date. The list shows the percent (and number) of pangrams containing solutions found to date that contain each word:
**The absolute numbers shown below are an INCORRECT OVERCOUNT. I won't fix this counting bug in the original stats script, but the relative ranking is probably still in the ballpark so I'm leaving this incorrect list in place until I have accurate data from post-processing after the final triple-check is complete.**
1. `WAQFS` : 27% (11086975) 
1. `VOZHD` : 25% (10272975) 
1. `QUAWK` : 9% (3747417) 
1. `PHYNX` : 9% (3694401) 
1. `VIBEX` : 9% (3591374) 
1. `FJORD` : 7% (2872084) 
1. `JUMPY` : 7% (2845176) 
1. `QUICK` : 7% (2792904) 
1. `QUACK` : 7% (2719085) 
1. `JUMBY` : 6% (2460518) 
1. `FJELD` : 5% (2128664) 
1. `FIQHS` : 5% (2026786) 
1. `JIMPY` : 4% (1766330) 
1. `VEXED` : 4% (1730712) 
1. `JIVED` : 4% (1685341) 
1. `QUECK` : 4% (1646150) 
1. `JUDGY` : 4% (1639016) 
1. `FRITZ` : 4% (1594095) 
1. `SQUIZ` : 4% (1439120) 
1. `WALTZ` : 3% (1230203) 
1. `BLITZ` : 3% (1186288) 
1. `GLITZ` : 3% (1183859) 
1. `VIXEN` : 3% (1157340) 
1. `BLONX` : 3% (1154275) 
1. `JOCKY` : 3% (1104606)


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
- 02025 Apr 06 - https://www.nytimes.com/shared/comment/46lgvt
- 02025 May 11 - https://www.nytimes.com/shared/comment/47f1r2
- 02025 May 18 - https://www.nytimes.com/shared/comment/47jvne
- 02025 Jun 07 - https://www.nytimes.com/shared/comment/482af8
- 02025 Jun 14 - https://www.nytimes.com/shared/comment/487h4e
