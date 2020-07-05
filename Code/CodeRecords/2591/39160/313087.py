t=int(input())

for i in range(t):
    n = int(input())
    n = n+2
    flag = 1
    for i in range(2,n):
        if(n%i == 0):
            flag = 0
            break
    if(flag == 0):
        print("No")
    else:
        print("Yes")