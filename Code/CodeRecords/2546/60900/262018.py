n = int(input())
a =[]
for i in range(0,n):
    a.append (int(input()))

def fun(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return (fun(n-2) + fun(n-3))

for i in range(0,n):
    print(fun(a[i]))