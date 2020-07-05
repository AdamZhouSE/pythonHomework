def divisorsSum(x):
    sum = x
    for i in range(1,x):
        if x%i == 0:
            sum += i
    return sum
test_num = int(input())
for i in range(test_num):
    n = int(input())
    if divisorsSum(n) < 2*n:
        print("1")
    else:
        print("0")