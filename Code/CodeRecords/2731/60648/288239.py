n=int(input())
for i in range(n):
    m=int(input())
    l=input().split(' ')
    ll=[]
    r=0
    for j in l:
        if j not in ll:
            ll.append(j)
    for j in ll:
        r+=l.count(j)//2
    print(r*2)