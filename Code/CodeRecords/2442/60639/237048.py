tup = input()
tup=tup.strip('[')
tup=tup.strip(']')
list=tup.split(',',)
n=len(list)
if n>=2:
    temp = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if int(list[i]) <= int(list[j]):
                continue
            else:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                break
    diff = []
    for i in range(0, n - 1):
        diff.append(int(list[i + 1]) - int(list[i]))
    result = max(diff)
    print(result)
else:
    print(0)