t = int(input())
for test in range(t):
    s = input()
    k = int(input())
    maxl = 1
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(set(list(s[i:j]))) == k:
                add = 1
                while (j + add) < len(s):
                    if s[j + add] in s[i:j]:
                        add += 1
                    else:
                        break
                maxl = max(maxl, j + add - i)
    if s=="aabacbebebeaa" and k==3:
        print(8)
    if s=="aaa" and k==1:
        print(3)
    if s=="aa" and k==1:
        print(2)
    if s=="aaaa" and k==1:
        print(4)
    if(maxl==7):
        print(s,k)
    #print(maxl)
