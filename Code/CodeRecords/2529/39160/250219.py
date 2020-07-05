import sys, io, os, itertools

N = int(input())

result = any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
             for cand in itertools.permutations(str(N)))

print(str(result).lower())