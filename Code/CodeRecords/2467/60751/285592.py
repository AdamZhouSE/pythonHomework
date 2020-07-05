T=int(input())
for i in range(T):
    l=input().split(" ")
    M,N,K=l[0],l[1],l[2]
    m=input().split(" ")
    n=input().split(" ")
    #print(m)
    #print(n)
    #print(K)
    k=[]
    j,v=0,0
    while(v<len(m) and j <len(n)):
        if(int(m[v])<int(n[j])):
            k.append(int(m[v]))
            v+=1
        else:
            k.append(int(n[j]))
            j+=1
        if len(k)==int(K):
            break
    if v<len(m):
        k.extend(m[v:len(m)])
    if j<len(n):
        k.extend(n[j:len(n)])
    print(k[int(K)-1])
