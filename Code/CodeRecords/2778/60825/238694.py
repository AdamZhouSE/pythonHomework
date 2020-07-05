N=int(input())
for i in range(N):
    a=input()
    l=a.split()
    l= list(map(int, l))
    L=l[0]
    R=l[1]
    ct=0
    for j in range(L,R+1):
        num=str(j)
        if num[0]==num[len(num)-1]:
            ct++
    print(ct)