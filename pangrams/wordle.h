// Copyright (C) Dez Moleski dez@moleski.com
// MIT License: All uses allowed with attribution.
#ifndef __WORDLE_H_INCLUDED
#define __WORDLE_H_INCLUDED

#include <stdint.h>

#define CHARMASK_A 0x00000001
#define CHARMASK_B 0x00000002
#define CHARMASK_C 0x00000004
#define CHARMASK_D 0x00000008
#define CHARMASK_E 0x00000010
#define CHARMASK_F 0x00000020
#define CHARMASK_G 0x00000040
#define CHARMASK_H 0x00000080
#define CHARMASK_I 0x00000100
#define CHARMASK_J 0x00000200
#define CHARMASK_K 0x00000400
#define CHARMASK_L 0x00000800
#define CHARMASK_M 0x00001000
#define CHARMASK_N 0x00002000
#define CHARMASK_O 0x00004000
#define CHARMASK_P 0x00008000
#define CHARMASK_Q 0x00010000
#define CHARMASK_R 0x00020000
#define CHARMASK_S 0x00040000
#define CHARMASK_T 0x00080000
#define CHARMASK_U 0x00100000
#define CHARMASK_V 0x00200000
#define CHARMASK_W 0x00400000
#define CHARMASK_X 0x00800000
#define CHARMASK_Y 0x01000000
#define CHARMASK_Z 0x02000000

#define CHARMASK_A_Z  0x03FFFFFF
#define CHARMASK_NONE 0x00000000

typedef struct
{
  char     word[6];
  char     letters[6];
  uint32_t letters_mask;
  uint8_t  letters_len;
  uint16_t anagrams_index;
  
} WordleWord;

typedef struct
{
  char     letters[6];
  uint8_t  len;
  uint16_t anagrams[16];

} WordleAnagram;

// Set up the anagrams_index for each WordleWord in ALL_WORDS.
extern void init_anagrams_indices(void);

#endif //  __WORDLE_H_INCLUDED
