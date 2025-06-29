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
**Updated 20 June 2025** (views 1754)

**Headline:** double and triple checks have passed, counts given below are mostly final (though subject to expected changes in the solutions list). The ranking of words by how many solution-bearing pangrams contain that word is still based on overcounts (this will be fixed eventually).

**Fast Pruning Algorithm**

My son found an amazing optimization of the search by pruning dead ends using a cleverly constructed cache of search state whenever a dead end is discovered. This enables the entire search to run in a single instance of the search program within about an hour on my main laptop! He also wrote his version of the search from scratch, AND ran it in parallel on a GPU, further reducing the run time to just a few minutes. **So proud of him!** and yet humbled that I never thought of these optimizations.

**Double and Triple Checking**

Because the slower searcher was so close to finishing its run though, I let it run to completion. But I also added my own implementation of the fast pruning to make a third version of the searcher. Upon checking the slow searcher results against both my and my son's implementation of the new fast-pruner, none of the 3 result sets matched!

However, the difference between my and my son's fast pruners was relatively easy to diagnose as what looked like a simple off-by-one error in his version (score one for the old man!) and apart from that they agreed to 99.999989% (6 pangrams missing out of 54.47 million: postscript - it turned out to be a side effect in an assert, not strictly an off-by-one). The slow searcher was a different story...

**Slow Searcher History and Results**

The final slow search program was run on up to twelve computers, with multiple instances per computer, but I let several of the slowest go idle, thinking I might write improved distributed search management code to reduce the manual tending that took up to an hour each day. But I hit an equilibrium and a pace of progress I could live with (about 1 hour overhead per week and 2% progress) and never did write the fancy search management system.

The earliest version of the slow searcher was written in python, which clearly had some relatively significant flaws (or else the all-too-human operator of that program made mistakes). After finally fixing things up by re-running the entire letter K, it remains a small mystery whether it was a bug in old code or human error that caused the problems in the K-data.

Bottom line is that after re-running the portion of the search that didn't match the fast pruners, which was in the range of K-P only (i.e. the search results starting from A through J, and Q through Z all matched the fast pruners' results), all the errors were in fact only in the searches from words starting with K, and the discrepancies in M-P were due to anagram expansions of K-words. All three data sets match after this last correction.

Finally, my post-processing scripts that provide the counts below are mostly dependent on the data format used by the slow searcher, which is just different enough from the fast pruners' output that I haven't re-written them (yet) to work from the better data provided by the fast pruners. Just another reason that I wanted to get the slow-search data to match results from the fast-pruners.

##### Counts
- 32,358,870 "base" Wordleable pangrams (without expanding anagrams) were found.
- 54,470,144 total Wordleable pangrams (with anagrams expanded) were found.
- 37,421,839 pangrams (68.7%) contain at least one known potential solution.
- 13,862 of 14,855 valid guesses (93%) appear in these pangrams.
- 2,225 of 2,326 known potential solutions (95.66%) appear in these pangrams.

The following 101 known potential solutions (4.34%) are not found in any pangram.
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

Top 50 words occurring in pangrams containing solutions. The list shows the percent (and number) of pangrams containing solutions found that contain each word (* indicates the word itself is a known potential solution):
1. `WAQFS`  : 26% (9,812,605) 
1. `VOZHD`  : 25% (9,173,872) 
1. `PHYNX`  :  9% (3,391,283) 
1. `QUAWK`  :  9% (3,325,194) 
1. `VIBEX`  :  9% (3,322,065) 
1. `FJORD`* :  8% (2,872,084) 
1. `JUMPY`* :  8% (2,845,176) 
1. `QUICK`* :  7% (2,792,910) 
1. `QUACK`* :  7% (2,719,095) 
1. `JUMBY`  :  6% (2,122,386) 
1. `FIQHS`  :  5% (1,911,577) 
1. `FJELD`  :  5% (1,904,839) 
1. `VEXED`  :  4% (1,612,513) 
1. `FRITZ`* :  4% (1,594,095) 
1. `JIMPY`  :  4% (1,580,090) 
1. `JIVED`  :  4% (1,556,037) 
1. `JUDGY`  :  4% (1,470,095) 
1. `QUECK`  :  4% (1,453,228) 
1. `SQUIZ`  :  4% (1,360,372) 
1. `WALTZ`* :  3% (1,230,223) 
1. `BLITZ`* :  3% (1,186,288) 
1. `VIXEN`* :  3% (1,157,491) 
1. `GLITZ`  :  3% (1,075,438) 
1. `BLONX`  :  3% (1,040,214) 
1. `JOCKY`  :  3%   (953,657) 
1. `QOPHS`  :  3%   (947,182)
1. `JAMBS`  :  3%   (946,046)
1. `JUMBO`* :  2%   (933,604) 
1. `VITEX`  :  2%   (915,549)
1. `VOXEL`  :  2%   (896,269)
1. `BUXOM`* :  2%   (845,828) 
1. `GUQIN`  :  2%   (840,115) 
1. `PHLOX`  :  2%   (835,688)
1. `JACKY`  :  2%   (835,383)
1. `QUBIT`  :  2%   (804,713)
1. `QAPIK`  :  2%   (800,603)
1. `BORTZ`  :  2%   (771,645)
1. `KLUTZ`  :  2%   (764,054)
1. `VEXIL`  :  2%   (739,236)
1. `JUMPS`  :  2%   (710,609)
1. `GLYPH`* :  2%   (661,088) 
1. `BOXTY`  :  2%   (631,444) 
1. `ZIMBS`  :  2%   (613,198) 
1. `ZYGON`  :  2%   (599,747) 
1. `BANTZ`  :  2%   (597,463)
1. `PYXED`  :  2%   (590,059)
1. `PLOTZ`  :  2%   (588,892) 
1. `CEZVE`  :  2%   (575,685)
1. `FLAXY`  :  1%   (554,593)
1. `ZINGY`  :  1%   (521,973)

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
- 02025 Jun 19 - https://www.nytimes.com/shared/comment/48b496
- 02025 Jun 20 - https://www.nytimes.com/shared/comment/48buh3
- 02025 Jun 27 - https://www.nytimes.com/shared/comment/48gfmf
