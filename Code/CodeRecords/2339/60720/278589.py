t=int(input())
for k in range(t):
    n=int(input())
    list0=input().split()
    for i in range(n):
        list0[i]=int(list0[i])
    sum=0
    for i in range(n):
        for j in range(i+1,n):
            if list0[i]>list0[j]:
                sum+=1
    print(sum)