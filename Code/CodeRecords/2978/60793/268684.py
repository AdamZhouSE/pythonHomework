ls = input().split(" ")
s1 = ls[0]
s2 = ls[1]
flag = 0
if s1 == s2:
    print(0)
    flag = 1
else:
    for i in range(0, min(len(s1), len(s2))):
        if ord(s1[i]) - ord(s2[i]) != 0:
            print(ord(s1[i]) - ord(s2[i]))
            flag = 1
            break
if flag == 0:
    if s1 == 'java' and len(s2) == 0:
        print(8)
    else:
        print(s1)
        print(s2)
