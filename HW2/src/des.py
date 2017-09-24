import binascii
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

def divide_by_six(split_num):
    return [split_num[i:i+6] for i in range(0, len(split_num), 6)]

def hex_to_bin(hex_num):
    return ''.join([hex2bin[x] for x in list(hex_num)])

def xor(rhs, lhs):
    return '{1:0{0}b}'.format(len(rhs), int(rhs, 2) ^ int(lhs, 2))

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
print('K_1 (hex): ', bin_to_hex(divide_by_four(K_1)), '\n')

# 2. Use this key to perform the round 1 encryption of the plaintext. This
#    involves the following steps:
# ------------------------
# a) Convert the Plaintext into binary

plaintext = 'MESSAGES' 
bin_plaintext = ''.join(format(ord(x), 'b').zfill(8) for x in plaintext)

print('STEP 2a')
print('-----------------')
print('Original plaintext: ', plaintext)
print('Plaintext (hex): ', bin_to_hex(divide_by_four(bin_plaintext)))
print('Plaintext (bin): ', ' '.join(divide_by_four(bin_plaintext)), '\n')

# b) Apply the initial permutation and break the plaintext into left and right
#    halves L_0 and R_0.

ip = ''
for num in init_perm:
    ip += str(bin_plaintext[num-1])

l_0 = ip[:len(ip) // 2]
r_0 = ip[len(ip) // 2:]

print('STEP 2b')
print('-----------------')
print('Plaintext (bin): ', ' '.join(divide_by_four(bin_plaintext)))
print('IP: ', ' '.join(divide_by_four(ip)))
print('L_0: ', ' '.join(divide_by_four(l_0)))
print('R_0: ', ' '.join(divide_by_four(r_0)), '\n')

# c) Expand R_0 to get E(R_0).

e_r0 = ''
for num in exp_perm:
    e_r0 += str(r_0[num-1])

print('STEP 2c')
print('-----------------')
print('R_0: ', ' '.join(divide_by_four(r_0)))
print('E(R_0): ', ' '.join(divide_by_four(e_r0)), '\n')

# d) Calculate A = E(R_0) ^ K1.

A = xor(e_r0, K_1)

print('STEP 2d')
print('-----------------')
print('E(R_0): ', ' '.join(divide_by_four(e_r0)))
print('K_1 (bin): ', ' '.join(divide_by_four(K_1)))
print('A: ', ' '.join(divide_by_four(A)), '\n')

# e) Group the 48-bit result A into sets of 6 bits and evaluate the
#    corresponding S-box substitutions.

A_1 = divide_by_six(A)

s_box_results = []
for i in range(0, len(A_1)):
    row_idx = int(A_1[i][0]+A_1[i][-1], 2)
    col_idx = int(A_1[i][1:-1], 2)

    s_box_results.append(format(int(s_boxes[i][row_idx][col_idx]), '04b'))

print('STEP 2e')
print('-----------------')
print('A_0: ', ' '.join(divide_by_four(A)))
print('A_1: ', ' '.join(A_1))

for i in range(0, len(A_1)):
    print('S'+str(i+1)+': ', s_box_results[i])
print('')

# f) Concatenate the results of e) to get a 32-bit result B.

B = ''.join(s_box_results)

print('STEP 2f')
print('-----------------')
print('B: ', ' '.join(divide_by_four(B)), '\n')

# g) Apply the permutation to get P(B).

P_B = ''
for num in perm:
    P_B += str(B[num-1])

print('STEP 2g')
print('-----------------')
print('B: ', ' '.join(divide_by_four(B)))
print('P_B: ', ' '.join(divide_by_four(P_B)), '\n')

# h) Calculate R_1 = P(B) ^ L_0.

R_1 = xor(P_B, l_0)

print('STEP 2h')
print('-----------------')
print('P_B: ', ' '.join(divide_by_four(P_B)))
print('L_0: ', ' '.join(divide_by_four(l_0)))
print('R_1 (bin): ', ' '.join(divide_by_four(R_1)))
print('R_1 (hex): ', bin_to_hex(divide_by_four(R_1)))

