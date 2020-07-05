n=int(input())
flag=True
strr=input()
char1=strr[0]
char2=strr[1]
if char1==char2:
    flag=False
for i in range(0,n):
    tmp=strr
    for j in range(0,n):
        if (i==j)or(i+j==n-1):
            if tmp[j]!=char1:
                flag=False
        else:
            if tmp[j]!=char2:
                flag=False
        if flag==False:
            break
    if flag==False:
        break
    if i!=n-1:
        strr=input()
if flag==True:
    print("YES")
else:
    print("NO")