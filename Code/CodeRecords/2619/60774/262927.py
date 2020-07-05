n = int(input())
result = []
for i in range(0,n):
    target = input()
    record = []
    flag = 1
    for s in range(0,len(target)):
        temp = int(target[s])
        if(temp in record):
            flag = 0
            break
        record.append(temp)
        for t in range(s + 1,len(target)):
            temp = temp * int(target[t])
            if(temp in record):
                flag = 0
                break
            record.append(temp)
    result.append(flag)
for item in result:
    print(item)