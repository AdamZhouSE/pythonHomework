N,K = [int(x) for x in input().split()]
centers = []
for i in range(N):
    centers.append([int(x) for x in input().split()])

def check(i,j):
    x1,y1 = centers[i]
    x2,y2 = centers[j]
    if (K-abs(x1-x2))>0 and (K-abs(y1-y2))>0:
        return (K-abs(x1-x2))*(K-abs(y1-y2))
    else:
        return 0
s = 0
summ  =0
for i in range(N):
    for j in range(i+1,N):
        now = check(i,j)
        if now>0:
            s+=1
            summ+=now
if s>1:
    print(-1)
else:
    print(summ)