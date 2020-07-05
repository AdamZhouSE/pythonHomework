n,t,c = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
method = 0
for i in range(n-c+1):
    yes = True
    for k in range(c):
        if(a[i+k] >t):
            yes = False
            break
    if(yes):
        method +=1
print(method)