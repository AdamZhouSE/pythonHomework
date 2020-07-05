from itertools import permutations


def judge():
    for i in permutations(input()):
        if i[0] == '0':
            break
        if bin(int(''.join(i))).count('1') == 1:
            return True
    return False


print(judge())
