num=int(input())
arr=[int(n) for n in input().split(' ')]
mark=0
for i in range(0,num):
    a=arr[i]
    for j in range(i+1,num):
        b=arr[j]
        for k in range(j+1,num):
            c=arr[k]
            if a<b+c and b<a+c and c<a+b:
                mark=1
                break
            else:
                continue
        if mark==1:
            break
    if mark==1:
        break
if mark==1:
    print('YES')
else:
    print('NO')