p=int(input())
for i in range(p):
    m,n=map(int,input().split(' '))
    ls=input().split(' ')
    ls=[int(ls[i]) for i in range(m)]
    #temp=0
    #print(ls)
    ll=[]
    for j in range(m-n+1):
        temp=0
        for k in range(n):
            if ls[j+k]>temp:
                temp=ls[j+k]
        ll.append(str(temp))
    s=" ".join(ll)
    print(s+" ")