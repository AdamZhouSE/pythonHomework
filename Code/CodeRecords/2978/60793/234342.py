import math
ls = input().split(" ")
s1 = ls[0]
s2 = ls[1]
flag = 0
if s1.__eq__(s2):
    print(0)
else:
    for i in range(0, min(len(s1), len(s2))):
        if ord(s1[i]) - ord(s2[i])!= 0:
            print(ord(s1[i]) - ord(s2[i]))
            flag = 1
            break
if flag == 0:
    if len(s1) < len(s2):
        print(ord(s2[len(s1)+1]))
    else:
        print(ord(s2[len(s2) + 1]))
    