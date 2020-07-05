n=int(input())
for q in range(n):
    n,m=map(int,input().split(' '))
    l=input().split(' ')
    ls=input().split(' ')
    ll=[]
    for i in l:
        if i not in ll:
            ll.append(i)
    for j in ls:
        if j not in ll:
            ll.append(j)
    print(len(ll))