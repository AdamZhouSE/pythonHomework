test_num = int(input())
result = 0
for i in range(test_num):
    n = int(input())
    A = input().split(" ")
    B = input().split(" ")
    C = input().split(" ")
    A = [int(x) for x in A]
    B = [int(x) for x in B]
    C = [int(x) for x in C]
    for j in range(n):
        temp = A[j] - B[j]
        for item in C:
            if temp == item:
                result += 1
    print(result)
