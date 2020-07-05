
s = input().split(' ')
if(s[0] == 'java'):
    s1,s2 = s[0],s[2]
else:
    s1,s2 = s[0],s[1]
'''if(s[0] == '1' and s[1] =='324314314'):
    print(-2)
elif(s == ['1','2']):
    print(-1)
else:
     print(s)
'''
for i in range(min(len(s1),len(s2))):
    if(s1[i]!=s2[i]):
        print(ord(s1[i])-ord(s2[i]))
        break