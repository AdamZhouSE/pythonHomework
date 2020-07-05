t = int(input())
for x in range(t):
    A = {}
    string = input()
    result = -1
    for x in range(len(string)):
        if string[x] not in A:
            A[string[x]] = x
        else:
            dis = x - A[string[x]] - 1
            if dis > result:
                result = dis
    print(result)
