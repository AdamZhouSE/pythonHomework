t = int(input())
for x in range(t):
    A = {}
    string = input()
    result = 0
    for x in range(len(string)):
        if string[x] not in A:
            A[string[x]] = [x]
        else:
            dis = x - A[string[x]]
            if dis > result:
                result = dis
    print(result)
