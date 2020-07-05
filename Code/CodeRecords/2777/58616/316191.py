t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(elem) for elem in input().split()]
    sortedArr = sorted(arr)
    if n%2 == 0:
        median = (sortedArr[(n//2)-1] + sortedArr[n//2]) / 2
    else:
        median = sortedArr[(n//2)]
    print(int(median))