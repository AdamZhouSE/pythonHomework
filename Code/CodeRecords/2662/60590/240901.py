tests = int(input())

lists = [ ]
for i in range(tests):
    a = int(input())
    lists.append(a)

result = []
for i in range(lists.__len__()):
    str = bin(int(lists[i]))
    arr = list(str)
    ones = 0
    if lists[i]>0:
        for j in range(2, arr.__len__()):
            if arr[j] == '1':
                ones = ones + 1
    elif lists[i]<0:
        #print(arr)
        for j in range(3, arr.__len__()):
            if arr[j] == '1':
                ones = ones + 1
    result.append(ones)

for i in range(result.__len__()):
    n = int(result[i])
    if n%2 ==0:
        print("even")
    else:
        print("odd")