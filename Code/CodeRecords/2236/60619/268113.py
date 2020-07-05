t = int(input())
data = []
for i in range(t):
    li = input().strip().split(" ")
    instru = int(li[0])
    target = int(li[1])
    if instru == 1:
        data.append(target)
        data.sort()
    elif instru == 2:
        ind = data.index(target)
        del(data[ind])
    elif instru == 3:
        print(data.index(target)+1)
    elif instru == 4:
        print(data[target-1])
    elif instru == 5:
        for j in range(len(data)):
            if data[j] > target:
                print(data[j-1])
                break
            elif j == len(data)-1:
                print(data[len(data)-1])
    elif instru == 6:
        for k in data:
            if k > target:
                print(k)
                break
