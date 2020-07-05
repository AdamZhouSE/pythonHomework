
a=[]
Square=[]
N=int(input())
for i in range(N):
    a.append(eval(input()))
for j in range(N-2):
    for k in range(j+1,N-1):
        for m in range(k+1,N):
            Square.append((abs((a[j][0]*a[k][1]-a[k][0]*a[j][1])+(a[k][0]*a[m][1]-a[m][0]*a[k][1]+(a[m][0]*a[j][1]-a[j][1]*a[m][1]))))/2)
print(max(Square))