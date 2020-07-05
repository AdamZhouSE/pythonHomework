data = eval(input())
find = True
for i in range(1, len(data) - 1):
    for j in range(1, i+1):
        if data[j] < data[j-1]:
            find = False
            break
    for j in range(i+1, len(data)):
        if data[j] > data[j-1]:
            find = False
            break
    if find:
        print(i)
        break
