tests = input()
tests = int(tests)
end=[]

for i in range(tests):
    arrEle, select = input().split()
    arrEle = int(arrEle)
    select = int(select)
    lists = list(map(int, input().split()))
    result = []
    for i in range(0,lists.__len__()+1-select):
        tempsum=0
        for j in range(i, i+select):
            tempsum += lists[j]
            result.append(tempsum)
    end.append(max(result))

for i in range(end.__len__()):
    print(end[i])