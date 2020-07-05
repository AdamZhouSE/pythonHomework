size=list(map(int,input().split('  ')))
s=input()
p1=size[0]
p2=size[1]
p3=size[2]
def issame(ch1,ch2):
    if(ord(ch1)>=97 and ord(ch1)<=122 and ord(ch2)>=97 and ord(ch2)<=122):
        return True
    elif(ord(ch1)>=48 and ord(ch1)<=57 and ord(ch2)>=48 and ord(ch2)<=57):
        return False
    return None
res=[]

for i in range(len(s)):
    tmp=""
    if(s[i]=='-'):
        if(issame(s[i-1],s[i+1])==True):
            if(p1==1):
                if (p3 == 2):
                    for j in range(ord(s[i + 1]) - 1, ord(s[i - 1]), -1):
                        for k in range(p2):
                            tmp += chr(j)
                    res.append(tmp)
                else:
                    for j in range(ord(s[i - 1]) + 1, ord(s[i + 1]), 1):
                        for k in range(p2):
                            tmp += chr(j)

                    res.append(tmp)
            elif(p1==2):
                if (p3 == 2):
                    for j in range(ord(s[i + 1]) - 1-32, ord(s[i - 1])-32, -1):
                        for k in range(p2):
                            tmp += chr(j)
                    res.append(tmp)
                else:
                    for j in range(ord(s[i - 1]) + 1-32, ord(s[i + 1])-32, 1):
                        for k in range(p2):
                            tmp += chr(j)
                    res.append(tmp)
            else:
                if (p3 == 2):
                    for j in range(ord(s[i + 1]) - 1, ord(s[i - 1]), -1):
                        for k in range(p2):
                            tmp +='*'
                    res.append(tmp)
                else:
                    for j in range(ord(s[i - 1]) + 1, ord(s[i + 1]), 1):
                        for k in range(p2):
                            tmp += '*'
                    res.append(tmp)
        elif(issame(s[i-1],s[i+1])==False):
            if(p1!=3):
                if(p3==2):
                    for j in range(ord(s[i+1])-1,ord(s[i-1]),-1):
                        for k in range(p2):
                            tmp+=chr(j)
                    res.append(tmp)
                else:
                    for j in range(ord(s[i-1])+1,ord(s[i+1]),1):
                        for k in range(p2):
                            tmp+=chr(j)
                    res.append(tmp)
            else:
                if (p3 == 2):
                    for j in range(ord(s[i + 1]) - 1, ord(s[i - 1]), -1):
                        for k in range(p2):
                            tmp +='*'
                    res.append(tmp)
                else:
                    for j in range(ord(s[i - 1]) + 1, ord(s[i + 1]), 1):
                        for k in range(p2):
                            tmp += '*'
                    res.append(tmp)
                
m=0
s=list(s)
for i in range(len(s)):
    if (s[i] == '-' and issame(s[i-1],s[i+1])!=None):
        s[i]=res[m]
        m+=1
print("".join(s))


