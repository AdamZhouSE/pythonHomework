n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    tmp1=0
    tmp2=0
    for i in range(0,l,2):
        tmp1+=int(a[i])
        if i+1<=l-1:
            tmp2+=int(a[i+1])
    print(max(tmp1,tmp2))
    #print(tmp2)