n = eval(input())
b = list(map(int,input().split(' ')))
a = [0]*n
a[-1] = b[-1]
for i in range(n-1,0,-1):
    a[i-1] = b[i-1] + b[i]
print(' '.join(map(str,a)))