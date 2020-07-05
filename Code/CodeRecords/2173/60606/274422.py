test_num = int(input())
for i in range(test_num):
    n = int(input())
    sum = 0
    for j in range(1,n+1):
        sum += (2*j-1)*(n+1-j)
    print(sum)