// Copyright (C) 2024 Dez Moleski dez@moleski.com
// MIT License: All uses allowed with attribution.
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <signal.h>
#include <string.h>
#include <unistd.h> // sleep

#include "all_words.inl"
#include "wordle.c" // yes, weird, but that's how it's meant to be done

int count_letters(uint32_t mask) {
  int n = 0;
  for(uint32_t b = CHARMASK_A; b <= CHARMASK_Z; b <<= 1)
    if (b & mask) ++n;
  return n;
}

int count_vowels(uint32_t mask) {
  int n = 0;
  if (mask & CHARMASK_A) ++n;
  if (mask & CHARMASK_E) ++n;
  if (mask & CHARMASK_I) ++n;
  if (mask & CHARMASK_O) ++n;
  if (mask & CHARMASK_U) ++n;
  if (mask & CHARMASK_Y) ++n;
  if (mask & CHARMASK_W) ++n;
  return n;
}

//#define WORDS ALL_WORDS
//#define N N_WORDS
#define WORDS NO_ANAGRAMS
#define N N_NO_ANAGRAMS

volatile sig_atomic_t sighup_received = 0;
void sighup_handler(int sig)
{
  sighup_received = 1;
}

volatile sig_atomic_t sigusr1_received = 0;
void sigusr1_handler(int sig)
{
  sigusr1_received = 1;
}

volatile sig_atomic_t sigusr2_received = 0;
void sigusr2_handler(int sig)
{
  sigusr2_received = 1;
}

void print_anagrams(int w)
{
  // The given int w is an index into the WORDS array, which contains ALL_WORDS indices.
  int word_index = WORDS[w];
  WordleWord *pw = ALL_WORDS + word_index;
  if (pw->anagrams_index) {
    printf("Anagrams of %s: [", pw->word);
    int a = pw->anagrams_index;
    int last = ANAGRAMS[a].len - 1;
    for(int j=0; j<=last; ++j) {
      int index = ANAGRAMS[a].anagrams[j];
      printf("%s", ALL_WORDS[index].word);
      if (j < last) {
	printf("|");
      } else {
	printf("]\n");
      }
    }
    fflush(stdout);
  }
}

void main(int argc, char **argv)
{
  // Handle SIGHUP to exit gracefully.
  signal(SIGHUP, sighup_handler);

  // Handle SIGUSR1 to print some information.
  signal(SIGUSR1, sigusr1_handler);
  
  // Handle SIGUSR2 to pause and restart the search.
  signal(SIGUSR2, sigusr2_handler);
  
  // Set up the anagrams_index for each WordleWord in ALL_WORDS.
  init_anagrams_indices();

  // The zero'th element of the ALL_WORDS array is empty.
  // This lets us use word index zero to mean "no word" analogous to '\0' meaning "no char"
  // We can also call this the null word (analogous to null char)
  
  // Just for symmetry: a0 is the initial alphabet mask, all 26 letters.
  uint32_t a0 = CHARMASK_A_Z;
  // a1, a2, etc. are the alphabet letters remaining at each level.
  uint32_t a1, a2, a3, a4, a5, a6;
  uint32_t n_pangrams_found; // count of pangrams found per word
  bool b_print_n_found; // can we trust & print n_pangrams_found?
  uint64_t n1=0, n2=0, n3=0, n4=0, n5=0, n6=0; // iteration counter at each level.
  uint64_t ln1=0, ln2=0, ln3=0, ln4=0, ln5=0, ln6=0; // "last" iteration counter at each level.
  WordleWord *pw1,*pw2,*pw3,*pw4,*pw5,*pw6;
  int r2, r3, r4, r5;
  int v2, v3, v4, v5;
  char *skip1 = NULL;
  char *skip2 = NULL;
  char *skip3 = NULL;
  char *skip4 = NULL;
  char *skip5 = NULL;
  char *skip6 = NULL;
  
  // Look for words to skip ahead to on command line.
  if (argc > 1) {
    if (strlen(argv[1]) == 5) {
      skip1 = argv[1];
    }
  }
  if (argc > 2) {
    if (strlen(argv[2]) == 5) {
      skip2 = argv[2];
    }
  }
  if (argc > 3) {
    if (strlen(argv[3]) == 5) {
      skip3 = argv[3];
    }
  }
  if (argc > 4) {
    if (strlen(argv[4]) == 5) {
      skip4 = argv[4];
    }
  }
  if (argc > 5) {
    if (strlen(argv[5]) == 5) {
      skip5 = argv[5];
    }
  }
  if (argc > 6) {
    if (strlen(argv[6]) == 5) {
      skip6 = argv[6];
    }
  }
  
  for(int w1 = 0; w1 < N; ++w1,++n1) {
    pw1 = ALL_WORDS + WORDS[w1];

    // Check for a skip-to at this level
    if (skip1 != NULL) {
      if (strcmp(pw1->word, skip1) < 0) {
	continue;
      } else {
	fprintf(stderr, "SKIP-TO(1): %s\n", pw1->word);
	fflush(stderr);
	skip1 = NULL;
      }
    }
    
    a1 = a0 & ~(pw1->letters_mask);
    
    // Reset the count of pangrams found for this word.
    // Note that if there are SKIPS below level 0, then
    // we can't rely on this counter and won't print it
    // for this word.
    n_pangrams_found = 0;
    b_print_n_found = true;
    for(int w2 = w1+1; w2 < N; ++w2,++n2) {
      pw2 = ALL_WORDS + WORDS[w2];
      
      // Check for a skip-to at this level
      if (skip2 != NULL) {
	b_print_n_found = false;
	if (strcmp(pw2->word, skip2) < 0) {
	  continue;
	} else {
	  fprintf(stderr, "SKIP-TO(2): %s\n", pw2->word);
	  fflush(stderr);
	  skip2 = NULL;
	}
      }
      
      // Skip word if it can't reduce the alphabet remaining.
      if ((a1 & pw2->letters_mask) == 0) continue;
      // Mask off this word's letters to get the next alpha remains.
      a2 = a1 & ~(pw2->letters_mask);
      // If the remaining alphabet has more letters than we could possibly remove, continue.
      r2 = count_letters(a2);
      if (r2 > 20) continue;
      // If the remaining alphabet is equal remaining letters, then the only solution
      // from here down is a heterogram over the remaining letters. That requires
      // at least as many vowels (counting W & Y liberally) as words remaining.
      if (r2 == 20) {
	v2 = count_vowels(a2);
	if (v2 < 4) continue;
      }
      /*
	fprintf(stderr, "%s %s %08x %d\n",
	     pw1->word,
	     pw2->word, a2, r2);
	fflush(stderr);
      */
      for(int w3 = w2+1; w3 < N; ++w3,++n3) {
	pw3 = ALL_WORDS + WORDS[w3];
	
	// Check for a skip-to at this level
	if (skip3 != NULL) {
	  b_print_n_found = false;
	  if (strcmp(pw3->word, skip3) < 0) {
	    continue;
	  } else {
	    fprintf(stderr, "SKIP-TO(3): %s\n", pw3->word);
	    fflush(stderr);
	    skip3 = NULL;
	  }
	}
	
	if ((a2 & pw3->letters_mask) == 0) continue;
	a3 = a2 & ~(pw3->letters_mask);
	r3 = count_letters(a3);
	if (r3 > 15) continue;
	if (r3 == 15) {
	  v3 = count_vowels(a3);
	  if (v3 < 3) continue;
	}
	
	for(int w4 = w3+1; w4 < N; ++w4,++n4) {
	  pw4 = ALL_WORDS + WORDS[w4];
	  
	  // Check for a skip-to at this level
	  if (skip4 != NULL) {
	    b_print_n_found = false;
	    if (strcmp(pw4->word, skip4) < 0) {
	      continue;
	    } else {
	      fprintf(stderr, "SKIP-TO(4): %s\n", pw4->word);
	      fflush(stderr);
	      skip4 = NULL;
	    }
	  }
	  
	  if ((a3 & pw4->letters_mask) == 0) continue;
	  a4 = a3 & ~(pw4->letters_mask);
	  r4 = count_letters(a4);
	  if (r4 > 10) continue;
	  if (r4 == 10) {
	    v4 = count_vowels(a4);
	    if (v4 < 2) continue;
	  }
	  
	  for(int w5 = w4+1; w5 < N; ++w5,++n5) {
	    pw5 = ALL_WORDS + WORDS[w5];
	    
	    // Check for a skip-to at this level
	    if (skip5 != NULL) {
	      b_print_n_found = false;
	      if (strcmp(pw5->word, skip5) < 0) {
		continue;
	      } else {
		fprintf(stderr, "SKIP-TO(5): %s\n", pw5->word);
		fflush(stderr);
		skip5 = NULL;
	      }
	    }
	    
	    if ((a4 & pw5->letters_mask) == 0) continue;
	    a5 = a4 & ~(pw5->letters_mask);
	    r5 = count_letters(a5);
	    if (r5 > 5) continue;
	    if (r5 == 5) {
	      v5 = count_vowels(a5);
	      if (v5 < 1) continue;
	    }
	    
	    for(int w6 = w5+1; w6 < N; ++w6,++n6) {
	      pw6 = ALL_WORDS + WORDS[w6];
	      
	      // Check for a skip-to at this level
	      if (skip6 != NULL) {
		b_print_n_found = false;
		if (strcmp(pw6->word, skip6) < 0) {
		  continue;
		} else {
		  fprintf(stderr, "SKIP-TO(6): %s\n", pw6->word);
		  fflush(stderr);
		  skip6 = NULL;
		}
	      }
	      
	      // Check for signal to exit gracefully.
	      // Print this to both stderr and stdout?
	      if (sighup_received) {
		printf("LAST: %s %s %s %s %s %s\n",
		       pw1->word,
		       pw2->word,
		       pw3->word,
		       pw4->word,
		       pw5->word,
		       pw6->word);
		exit(0);
	      }
	      
	      // Check for signal to print some information and continue,
	      // or to pause the search here (SIGUSR2) until signaled again.
	      if (sigusr1_received || sigusr2_received) {
		sigusr1_received = 0;
		fprintf(stderr, "STACK: %s %s %s %s %s %s\n",
			pw1->word,
			pw2->word,
			pw3->word,
			pw4->word,
			pw5->word,
			pw6->word);
		fprintf(stderr, "COUNTS: %lu %lu %lu %lu %lu %lu\n", n1, n2, n3, n4, n5, n6);
		fprintf(stderr, "DELTAS: %lu %lu %lu %lu %lu %lu\n", n1-ln1, n2-ln2, n3-ln3, n4-ln4, n5-ln5, n6-ln6);
		fflush(stderr);
		ln1=n1; ln2=n2; ln3=n3; ln4=n4; ln5=n5; ln6=n6;
		if (sigusr2_received) {
		  sigusr2_received = 0;
		  fprintf(stderr, "PAUSED ... ");
		  fflush(stderr);
		  while (sigusr2_received == 0) {
		    sleep(60); // signal should wake me up so it shouldn't matter how long I sleep
		  }
		  sigusr2_received = 0;
		  fprintf(stderr, "RESUMING!\n");
		  fflush(stderr);
		}
	      }
	      
	      if ((a5 & pw6->letters_mask) == 0) continue;
	      a6 = a5 & ~(pw6->letters_mask);

	      if (a6 == 0) {
		// We found a pangram.
		++n_pangrams_found;
		printf("%s %s %s %s %s %s\n",
		       pw1->word,
		       pw2->word,
		       pw3->word,
		       pw4->word,
		       pw5->word,
		       pw6->word);
		fflush(stdout);
		/* TODO: DEZ: check-pangrams does this for me now, don't bother here.
		print_anagrams(w1);
		print_anagrams(w2);
		print_anagrams(w3);
		print_anagrams(w4);
		print_anagrams(w5);
		print_anagrams(w6);
		*/
	      }  // end if
	    } // for w6
	  } // for w5
	} // for w4
      } // for w3
    } // for w2

    // If none of the nested loops had SKIPs, then print
    // the number of pangrams found for this word.
    if (b_print_n_found) {
      printf("# %s = %u\n", pw1->word, n_pangrams_found);
      fflush(stdout);
    }
    
  } // for w1
}
