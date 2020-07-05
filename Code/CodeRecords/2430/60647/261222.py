n=int(input())
for j in range(n):
    num=int(input())
    list=input().split()
    k=int(input())
    c=0
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if int(list[i])+int(list[j])==k:
                c=1
                print(list[i],end=" ")
                print(list[j],end=" ")
                print(k)
    if c==0:
        print("-1")