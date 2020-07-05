arr=input()[1:-1].split(',')
lower=int(input())
upper=int(input())

num=0
s=0
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            s=s+int(arr[k])
        if s>=lower and s<=upper:
            num=num+1
        s=0
print(num)
