n=int(input())
result=[]
while n>0:
    length=int(input())
    ls=[]
    ls=input().split(" ")
    can=0
    for i in range(len(ls)):
        s=ls[i]
        total=0
        for j in range(len(s)):
            total=total+int(s[j])
        ls[i]=total  #整数的数字和
    total=0  
    for i in range(len(ls)):
        total=total+ls[i]
    if total%3==0:
        can=1
    result.append(can)
    n=n-1
for i in range(0,len(result)):
    print(result[i])




