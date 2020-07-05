s = input()
s=' '.join(s.split())# 去除多个空格
l = s.split(" ")
s1 = l[0]
s2 = l[1]
situation = True
length = len(s1)

for x in range(length):
    if(s1[x] == s2[x]):
        continue
    else:
        situation = False
        print(ord(s1[x])-ord(s2[x]))
        break;
if(situation):
    print(0)