n=int(input())
number=[int(x) for x in input().split()]
jls,dm=0,0
head, tail=0,n-1
for i in range(n):
    if i%2==0:
        if number[head]>number[tail]:
            jls+=number[head]
            head+=1
        else:
            jls+=number[tail]
            tail-=1
    else:
        if number[head]>number[tail]:
            dm+=number[head]
            head+=1
        else:
            dm+=number[tail]
            tail-=1
print(jls,dm)