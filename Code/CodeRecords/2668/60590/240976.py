import math
tests = int(input())

lists = []
for i in range(tests):
    n = int(input())
    lists.append(n)

end = []
for i in range(lists.__len__()):
    str = bin(int(lists[i]))
    arr = list(str)
    if arr[0]=='-':
        for j in range(3, arr.__len__()):
            if arr[j] == '0':
                arr[j] = '1'
        result = 0
        for k in range(3, arr.__len__()):
            result = result + pow(2, arr.__len__()-1-k)
        result = -result
    else:
        for j in range(2, arr.__len__()):
            if arr[j] == '0':
                arr[j] = '1'
        result = 0
        for k in range(2, arr.__len__()):
            result = result + pow(2, arr.__len__()-1-k)

    sub = result - lists[i]
    temp = []
    temp.append(sub)
    temp.append(result)
    end.append(temp)

#print(end)
for i in range(end.__len__()):
    print(end[i][0], end=" ")
    print(end[i][1])