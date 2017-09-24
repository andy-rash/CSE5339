from tables import (hex2bin, bin2hex, PC_1, PC_2, exp_perm, \
                    init_perm, fin_perm, perm, rotations, s_boxes)



def shift_left(bin_num, shamt=1):
    bin_num = ''.join(bin_num)
    bin_num = bin_num[shamt:]+bin_num[:shamt]
    return [bin_num[i:i+4] for i in range(0, len(bin_num), 4)]

def bin_to_hex(bin_num):
    return ''.join([bin2hex[x] for x in list(bin_num)])

def divide_by_four(split_num):
    return [split_num[i:i+4] for i in range(0, len(split_num), 4)]

def hex_to_bin(hex_num):
    return ''.join([hex2bin[x] for x in list(hex_num)])

# ----------------------------------

input_key = '0123456789ABCDEF'
bin_input_key = hex_to_bin(input_key)

# 1. Derive the round 1 key K_1
# ------------------------
# a) Reduce the initial 64-bit key input to the requisite 56-bit key by mapping
#    the bits of the initial key through the Permuted Choice 1 (PC-1) box. 
#    (64 bits excluding every 8th bit = 56 bits. These removed 8-bits are
#    sometimes used as parity bits). 

init_reduce = ''
for num in PC_1:
    init_reduce += str(bin_input_key[num-1])
init_reduce_split = divide_by_four(init_reduce)
hex_init_reduce = bin_to_hex(init_reduce_split)

print('STEP 1a')
print('-----------------')
print('Input key (hex): ', input_key)
print('Input key (bin): ', ' '.join(divide_by_four(bin_input_key)))
print('Reduced K_0 (bin): ', ' '.join(init_reduce_split))
print('Reduced K_0 (hex): ', ''.join(hex_init_reduce), '\n')

# b) Perform the specified left shift on the 28-bit left and right halves.

c_0 = init_reduce_split[0:int(len(init_reduce_split)/2)]
d_0 = init_reduce_split[int((len(init_reduce_split)/2)):len(init_reduce_split)]

c_1 = shift_left(c_0)
d_1 = shift_left(d_0)

c_1d_1 = c_1 + d_1

print('STEP 1b')
print('-----------------')
print('C_0: ', ' '.join(c_0))
print('C_1: ', ' '.join(c_1))
print('D_0: ', ' '.join(d_0))
print('D_1: ', ' '.join(d_1), '\n')
print('C_1D_1: ', ' '.join(c_1d_1), '\n')

# c) Use the permutation (PC-2) to derive the 48-bit round 1 key K_1.

K_1 = ''
c_1d_1 = ''.join(c_1d_1)
for num in PC_2:
    K_1 += str(list(''.join(c_1d_1))[num-1])

print('STEP 1c')
print('-----------------')
print('K_1 (bin): ', ' '.join(divide_by_four(K_1)))
print('K_1 (hex): ', bin_to_hex(divide_by_four(K_1)))

