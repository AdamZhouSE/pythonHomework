questNum = int(input())

for i1 in range(questNum):
    n = int(input())
    triangle = input().split(' ')
    for index in range(n):
        triangle[index] = int(triangle[index])

    triangle.sort()

    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            twoSideSum = triangle[i] + triangle[j]
            for k in range(j + 1, n):
                if triangle[k] >= twoSideSum:
                    break
                else:
                    count += 1

    print(count)