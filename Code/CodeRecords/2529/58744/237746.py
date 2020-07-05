import itertools


def isPowerOf2(num) -> bool:
    return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                for cand in itertools.permutations(str(num)))

print(str(isPowerOf2(input())).lower())