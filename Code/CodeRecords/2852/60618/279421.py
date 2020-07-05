n=int(input())
food=[int(n) for n in input().split()]
maxlen=0
re=1
for i in range(0,n):
    for j in range(i,n):
        if food[j]!=food[i]:
            length=j-i
            if (2*j-i-1)<=n-1:
                for k in range(j,2*j-i):
                    if food[k]==food[i]:
                        re=0
            else:
                break
            if re==0:
                length=0
            else:
                if maxlen<length:
                    maxlen=length
                length=0
            break
print(maxlen)
                