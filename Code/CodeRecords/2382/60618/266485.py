n=int(input())
ab=[[0]*2]*n
for i in range(0,n):
    ab[i] = map(int,input().split())
for j in range(0,n):
    for k in range(0,n):
        if ab[j][1]>=ab[k][0] and ab[k][0]>=ab[j][0]:
            
    