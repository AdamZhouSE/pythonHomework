t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for i in range(n//10+1):
        for j in range(n//5+1):
            for k in range(n//3+1):
                if 3*k+5*j+10*i == n:
                    count+=1
    print(count)