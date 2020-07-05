p=int(input())
for i in range(p):
    m,n=map(int,input().split(' '))
    ls=input().split(' ')
    ls=[int(ls[i]) for i in range(m)]
    #temp=0
    ll=[]
    for j in range(m-2):
        temp=0
        for k in range(3):
            if ls[j+k]>temp:
                temp=ls[j+k]
        ll.append(str(temp))
    s=" ".join(ll)
    print(s)