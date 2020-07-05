import sys


def isEqual(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    return list1 == list2


def excute(S, word):
    count = 0
    for i in range(0, len(S) - len(word)+1):
        str = S[i:i + len(word)-1]
        if str==word:
            count += 1
    print(count)


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    S = Input[begin]
    word = Input[begin + 1]
    begin += 2
    excute(S, word)
