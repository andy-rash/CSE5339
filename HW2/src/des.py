from tables import (bin_map, PC_1, PC_2, exp_perm, init_perm, \
                   fin_perm, perm, rotations, s_boxes)

input_key = '0123456789ABCDEF'
bin_input_key = ''.join([bin_map[x] for x in list(input_key)])

# 1. Derive the round 1 key K_1
# ------------------------
# a) Reduce the initial 64-bit key input to the requisite 56-bit key by mapping
#    the bits of the initial key through the Permuted Choice 1 (PC-1) box. 
#    (64 bits excluding every 8th bit = 56 bits. These removed 8-bits are
#    sometimes used as parity bits). 



# b) Perform the specified left shift on the 28-bit left and right halves.

# c) Use the permutation (PC-2) to derive the 48-bit round 1 key K_1.
