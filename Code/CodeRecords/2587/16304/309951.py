num = int(input())
X=[]
Y=[]
ans = 0
for i in range(num):
    a = input().split(',')
    X.append(int(a[0]))
    Y.append(int(a[1]))
x0 = X[0]
x1 = Y[0]
for i in range(1,num):
    y0, y1 = X[i],Y[i]
    ans += max(abs(x0 - y0), abs(x1 - y1))
    x0, x1 = X[i],Y[i]
print(ans)
