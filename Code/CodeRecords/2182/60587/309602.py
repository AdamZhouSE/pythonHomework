T = int(input())
while T > 0:
    T -= 1
    n, k = input().split(' ')
    n = int(n)
    k = int(k)

    result = []
    num = 1
    peoples = [True for _ in range(n)]
    while any(peoples):
        for index, people in enumerate(peoples):
            if people:
                if num == k:
                    peoples[index] = False
                    result.append(index + 1)
                    num = 1
                else:
                    num += 1
    print(result[len(result) - 1])
