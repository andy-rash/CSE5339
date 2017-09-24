import glob
import os

hex2bin = { '0': '0000', '1': '0001', '2': '0010', '3': '0011',
            '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
            'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111' }
bin2hex = { v: k for k,v in hex2bin.items() }

# import all of the tables, etc.
PC_1 = []
with open('../res/PC1.dat', 'r') as fp:
    for line in fp:
        PC_1.append(int(line))

PC_2 = []
with open('../res/PC2.dat', 'r') as fp:
    for line in fp:
        PC_2.append(int(line))

exp_perm = []
with open('../res/e.dat', 'r') as fp:
    for line in fp:
        exp_perm.append(int(line))

init_perm = []
with open('../res/ip.dat') as fp:
    for line in fp:
        init_perm.append(int(line))

fin_perm = []
with open('../res/ip-1.dat', 'r') as fp:
    for line in fp:
        fin_perm.append(int(line))

perm = []
with open('../res/p.dat', 'r') as fp:
    for line in fp:
        perm.append(int(line))

rotations = {}
with open('../res/rotations.dat', 'r') as fp:
    for line in fp:
        line_split = line.split(',')
        rotations[line_split[0]] = line_split[1]

s_boxes = [ [], [], [], [],
            [], [], [], [] ]
for item in glob.glob('../res/s-boxes/*.dat'):
    n = 0
    num_list = []
    with open(item, 'r') as fp:
        if os.path.basename(fp.name) == 'S1.dat': 
            for line in fp:
                num_list.append(int(line))
                n += 1
                if n == 16:
                    s_boxes[0].append(num_list)
                    num_list = []
                    n = 0
        elif os.path.basename(fp.name) == 'S2.dat':
            for line in fp:
                num_list.append(int(line))
                n += 1
                if n == 16:
                    s_boxes[1].append(num_list)
                    num_list = []
                    n = 0 
        elif os.path.basename(fp.name) == 'S3.dat':
            for line in fp:
                num_list.append(int(line))
                n += 1
                if n == 16:
                    s_boxes[2].append(num_list)
                    num_list = []
                    n = 0 
        elif os.path.basename(fp.name) == 'S4.dat':
            for line in fp:
                num_list.append(int(line))
                n += 1
                if n == 16:
                    s_boxes[3].append(num_list)
                    num_list = []
                    n = 0 
        elif os.path.basename(fp.name) == 'S5.dat':
            for line in fp:
                num_list.append(int(line))
                n += 1
                if n == 16:
                    s_boxes[4].append(num_list)
                    num_list = []
                    n = 0 
        elif os.path.basename(fp.name) == 'S6.dat':
            for line in fp:
                num_list.append(int(line))
                n += 1
                if n == 16:
                    s_boxes[5].append(num_list)
                    num_list = []
                    n = 0 
        elif os.path.basename(fp.name) == 'S7.dat':
            for line in fp:
                num_list.append(int(line))
                n += 1
                if n == 16:
                    s_boxes[6].append(num_list)
                    num_list = []
                    n = 0 
        elif os.path.basename(fp.name) == 'S8.dat':
            for line in fp:
                num_list.append(int(line))
                n += 1
                if n == 16:
                    s_boxes[7].append(num_list)
                    num_list = []
                    n = 0

