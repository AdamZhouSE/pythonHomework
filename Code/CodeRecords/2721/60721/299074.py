T=int(input())
for i in range(0,T):
    m,n=map(list,input().split(" "))
    re=0
    m=[int(j) for j in m]
    for j in range(0,len(m)):
        re+=m[j]*int(pow(2,len(m)-1-j))
    re1=0
    n=[int(j) for j in n]
    for j in range(0,len(n)):
        re1+=n[j]*int(pow(2,len(n)-1-j))
    print(re*re1)