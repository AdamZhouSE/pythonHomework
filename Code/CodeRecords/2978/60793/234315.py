import math
ls = input().split(" ")
s1 = ls[0]
s2 = ls[1]
if s1.__eq__(s2):
    print(0)
else:
    for i in range(0, min(len(s1), len(s2))):
        if ord(s1[i]) - ord(s2[i])!= 0:
            print(ord(s1[i]) - ord(s2[i]))
            break
