from itertools import permutations
N = int(input())
N_str = str(N)
l = list(map(''.join, permutations(N_str)))
for s in l:
    if s[0] != "0":
        if int(s) & (int(s) - 1) == 0 or int(s) == 1:
            print(True)
            exit()
print(False)
