// This file is meant to be included in program code after including all_words.inl

// Set up the anagrams_index for each WordleWord in ALL_WORDS.
void init_anagrams_indices(void)
{
  for(int anagram_index = 1; anagram_index <= N_ANAGRAMS; ++anagram_index) {
    for(int a = 0; a < ANAGRAMS[anagram_index].len; ++a) {
      int w = ANAGRAMS[anagram_index].anagrams[a];
      ALL_WORDS[w].anagrams_index = anagram_index;
    }
  }
}
