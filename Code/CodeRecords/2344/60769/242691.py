num = int(input())
for i in range(num):
    n = int(input())
    arr1 = input().split(" ")
    k = int(input())
    print(" ".join(arr1[k:] + arr1[:k]),end=" ")
    print()
