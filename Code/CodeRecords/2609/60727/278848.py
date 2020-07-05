def so(li,n,k):
    temp = 0
    for i in li:
        if li.count(i)==1:
            temp+=1
            if temp==k:
                return i
    return -1
for i in range(0,eval(input())):
    nk = input().split(' ')
    n=int(nk[0])
    k=int(nk[1])
    li = input().split(' ')
    li = [int(x) for x in li]
    print(so(li,n,k))