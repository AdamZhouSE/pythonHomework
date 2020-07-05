test = int(input())
for t in range(test):
    n = int(input())
    arr = input().split(' ')
    even = ""
    odd = ""
    for x in arr:
        temp = int(x)
        if temp%2 == 0:
            even += x + " "
        else:
            odd += x + " "
    result = even + odd
    print(result)

























