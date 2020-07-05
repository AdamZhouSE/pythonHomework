import re
s=input()
s=re.sub(' +', ' ', s)
s=s.split(" ")
s1=s[0]
s2=s[1]
if len(s1)==len(s2):
    if s1==s2:
        print (0)
    else:
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                print(int(ord(s1[i]))-int(ord(s2[i])))
                break
            else:
                continue
elif len(s1)<len(s2):
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            print(int(ord(s1[i]))-int(ord(s2[i])))
            break
        else:
            continue
else:
     for i in range(len(s2)):
        if s1[i]!=s2[i]:
            print (int(ord(s1[i]))-int(ord(s2[i])))
            break
        else:
            continue