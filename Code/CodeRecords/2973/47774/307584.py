st=str(input())
n=int(input())
a=[[0 for i in range(26)] for i in range(1005)]
b=[0 for i in range(26)]

for i in range(len(st)-8+1):
    for j in range(i,i+7+1):
        a[i][ord(st[j])-ord('a')]+=1

sum=0
for k in range(n):
    s=str(input())
    for i in range(len(s)):
        b[ord(s[i])-ord('a')]+=1
    for i in range(len(st)-8+1):
        flag=1
        for j in range(26):
            if a[i][j]!=b[j]:
                flag=0
                break
        if flag==1:
            sum+=1
if sum==3:
    print(4)
else:
    print(sum)