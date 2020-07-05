t = input().split()
k = int(t[0])
m = int(t[1])
s = input()
n = int(input())
for i in range(0,n):
    op = input().split()
    a = int(op[0])
    b = int(op[1])
    c = int(op[2])
    temp = s[a:b]
    s = s[:c] + temp + s[c:]
    if(len(s) > m):
        s = s[:m]
print(s[:k],end = '')