n=eval(input())
string=input()
num=[int(n) for n in string.split()]
flag=0
index=0
for i in range(index,n-1):
    if(num[i]>=num[i+1]):
        break
    else:
        index=index+1
for i in range(index,n-1):
    if(num[i]!=num[i+1]):
        break
    else:
        index=index+1
for i in range(index,n-1):
    if(num[i]<=num[i+1]):
        break
    else:
        index=index+1
if(index==n-1):
    print("YES")
else:
    print("NO")