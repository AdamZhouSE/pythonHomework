n=eval(input())
num=input().strip().split(' ')
num=[int(i) for i in num]
i=n1=n2=n3=n4=result=0
for i in range(0,n):
    if num[i] == 1: n1 += 1
    if num[i] == 2: n2 += 1
    if num[i] == 3: n3 += 1
    if num[i] == 4: n4 += 1
result=n4+n2//2
n2=n2%2
if n3>=n1:
    result=result+n2+n3
else:
    result+=n3
    n1-=n3
    if n2==1:
        if n1<=2:
            result+=1
        elif (n1-2)%4!=0:
            result = result + 2 + (n1 - 2) // 4
        else:
            result = result + 1 + (n1 - 2) // 4
    else:
        if n1 % 4 != 0:
            result = result + n1 // 4 + 1
        else:
            result = result + n1 // 4
print(result)