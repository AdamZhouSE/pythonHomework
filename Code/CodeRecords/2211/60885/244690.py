def interest(names, k):
    result = []
    for i in range(k):
        front = input()
        count = 0
        for name in names:
            if name.startswith(front):
                count += 1
        result.append(count)
    return result

def buildNames(n):
    names = ['' for i in range(n)]
    for i in range(n):
        name, m = input().split()
        m = int(m)
        if m == 0:
            names[0] = name
        else:
            names[i] = name + names[m-1]
    # print(names)
    return names

n,k = list(map(int, input().split()))
names = buildNames(n)
result = interest(names, k)
for i in result:
    print(i)