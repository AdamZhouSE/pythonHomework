t=int(input())

for i in range(t):
    n = int(input())
    if (n-3)%3 == 0:
        j = int((n-3)/3)
        print(j,j+1,j+2)
    else:
        print("-1")