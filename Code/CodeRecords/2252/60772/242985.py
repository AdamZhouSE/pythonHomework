import sys


def isEqual(s1, s2):
    s1.sort()
    s2.sort()
    return s1 == s2


def excute(S, word):
    count = 0
    for i in range(0,len(S)-len(word)+1):
        temp = []
        for j in range(i,i+len(word)):
            temp.append(S[j])
        if isEqual(temp,word):
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
    S = list(Input[begin])
    word = list(Input[begin + 1])
    begin += 2
    S.pop()
    word.pop()
    excute(S, word)


