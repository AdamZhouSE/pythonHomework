import re
s=input()
if(s[len(s)-1:]==" "):
        s=s[0:len(s)-1]
n,m=map(int,s.split(" "))
lis=[]
b=[]
for i in range(0,n-1):
    s=re.findall(r"[0-9]{1,}",input())
    s=[int(j) for j in s]
    lis.append(s)
b.append(lis[0][0])
for o in range(0,m):
    s=input().split(" ")
    if(s[0]=="C"):
        b.append(int(s[1]))
    else:
        if(int(s[1]) in b):
            print(s[1])
        else:
            q=False
            while q!=True:
                for i in range(0,n-1):
                    if(lis[i][1]==int(s[1])):
                        if(lis[i][0] in b):
                            print(lis[i][0])
                            q=True
                            break
                        else:
                            s[1]=str(lis[i][0])
                            break
    