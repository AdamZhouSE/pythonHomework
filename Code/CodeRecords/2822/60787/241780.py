n=int(input())
one=[int(i) for i in input().split()]
two=[int(i) for i in input().split()]
m=1
for i in range(1,n+1):
    m*=i
m*=(n-1)
del one[0]
del two[0]
flag=True
num=0
while len(one)>0 and len(two)>0:
    if num>m:
        flag=False
        print(-1)
        break
    else:
        if one[0]>two[0]:
            one.append(two[0])
            one.append(one[0])
        else:
            two.append(one[0])
            two.append(two[0])
        del one[0]
        del two[0]
        num+=1
if flag:
    if len(one)==0:
        print(str(num)+" 2")
    else:
        print(str(num)+" 1")