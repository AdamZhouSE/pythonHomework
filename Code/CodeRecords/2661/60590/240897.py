tests = int(input())

lists = [ ]
for i in range(tests):
    a = int(input())
    lists.append(a)
#print(lists)

result = []
for i in range(lists.__len__()):
    str = bin(int(lists[i]))
    arr = list(str)
    zeros = 0
    ones = 0
    if lists[i]>0:
        for j in range(2, arr.__len__()):
            if arr[j] == '0':
                zeros = zeros + 1
            else:
                ones = ones + 1
    elif lists[i]<0:
        #print(arr)
        for j in range(3, arr.__len__()):
            if arr[j] == '0':
                zeros = zeros + 1
            else:
                ones = ones + 1
        #print(zeros)
        #print(ones)
    ans = zeros ^ ones
    result.append(ans)
#print(result)
for i in range(result.__len__()):
    print(result[i])
