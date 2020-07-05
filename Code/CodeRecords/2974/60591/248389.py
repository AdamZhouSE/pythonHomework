# -*- coding: utf-8 -*-
def isOk(string):
    if(len(string)%2==0):
        return False
    else:
        for x in range(int(len(string)/2)):
            if(string[x] != string[len(string) - 1 - x]):
                return False
    return True

n = eval(input())
string = input()
max = 0
for x in range(n - 1):
    string1 = string[0:x+1]
    string2 = string[x+1:]
    string1s = []
    string2s = []
    for m in range(len(string1)):
        for n in range(m + 1,len(string1) + 1):
            temp = string1[m:n]
            if(isOk(temp)):
                string1s.append(temp)
    string1s = set(string1s)
    for m in range(len(string2)):
        for n in range(m + 1,len(string2) + 1):
            temp = string2[m:n]
            if(not isOk(temp)):
                string2s.append(temp)
    string2s = set(string2s)
    count1 = len(string1s)
    count2 = len(string2s)
    if(count1 * count2 > max):
        max = count1 * count2
print(max)
