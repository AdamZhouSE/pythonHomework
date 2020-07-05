n = int(input())
t = []
for i in range(0,n):
    t.append(int(input()))

def fun(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        if x%2==1:
            return 1+fun(x-1)
        else:
            return 1+fun(int(x/2))

for i in range(0,n):
    print(fun(t[i]))