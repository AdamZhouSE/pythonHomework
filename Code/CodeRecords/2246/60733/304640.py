import itertools
N=int(input())
print(any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1 for cand in itertools.permutations(str(N))))

