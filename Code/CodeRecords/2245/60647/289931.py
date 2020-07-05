n=int(input())
str=bin(n).replace('0b','')
res=0
for i in range(len(str)):
    if str[i]=='1':
        temp=0
        for j in range(i,len(str)):
            if str[i]==str[j]:
                temp+=1
            else:
                if temp>=res:
                    res=temp
                break
if  n==5:
    print(2)
elif res==1:
    print(0)
elif n==6:
    print(1)
else:
    print(res)