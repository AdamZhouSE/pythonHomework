s1,s2=input().split()
if s1==s2:
    print(0)
else:
    for  i in range(min(len(s1),len(s2))):
        if s1[i]==s2[i]:
            continue
        else:
            print(ord(s1[i])-ord(s2[i]))
            break