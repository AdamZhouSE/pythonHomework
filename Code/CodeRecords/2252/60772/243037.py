import sys


def isEqual(s1, s2):
    s1.sort()
    s2.sort()
    return s1 == s2


def excute(S, word):
    count = 0
    list1 = []
    list2 = []
    for i in range(0,len(S)):
        if S[i].isalpha():
            list1.append(S[i])
    for i in range(0,len(word)):
        if word[i].isalpha():
            list2.append(word[i])

    for i in range(0,len(list1)-len(list2)+1):
        temp = []
        for j in range(i,i+len(list2)):
            temp.append(list1[j])
        if isEqual(temp,list2):
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
    excute(S, word)


