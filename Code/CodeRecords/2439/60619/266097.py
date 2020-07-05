t = int(input())
startP = []
endP = []
values = []
for i in range(t-1):
    li = input().strip().split(" ")
    startP.append(int(li[0]))
    endP.append(int(li[1]))
    values.append(int(li[2]))
count = int(input())
for i in range(count):
    li = input().split(" ")
    s = int(li[0])
    target = int(li[1])
    result = 0
    if s != target:
        while True:
            ind = startP.index(s)
            result = result ^ values[ind]
            if endP[ind] == target:
                break
            else:
                s = endP[ind]
    print(result)