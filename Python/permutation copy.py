from itertools import permutations
name, size = input().split()
size = int(size)
P_list = list(permutations(sorted(name), size))
for each in P_list:
    print(*each, sep='')