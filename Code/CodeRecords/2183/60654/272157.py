a = int(input())
for i in range(a):
    b = int(input())
    sum = 0 
    for j in range(b**2-b+1,(b+1)**2-b):
        sum += j
    print(sum)    