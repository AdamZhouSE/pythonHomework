import itertools

n=int(input())
if any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1 for cand in itertools.permutations(str(n))) :
    print("true")
else:
    print("false")
