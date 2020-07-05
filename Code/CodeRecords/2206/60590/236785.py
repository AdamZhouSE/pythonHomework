tests = int(input())

lists = []
for i in range(tests):
    temp = int(input())
    lists.append(temp)
#print(lists)

def func(num):
    result = 0
    ele = ((1+num)*num)/2
    ele = int(ele)
    lists = []
    for i in range(ele):
        lists.append(i+1)
    #print(lists)
    arr = []
    for i in range(1,num+1):
        #print(i)
        temp = []
        while i>0:
            temp.append(lists[0])
            lists.remove(lists[0])
            i = i-1
        arr.append(temp)
    #print(arr)

    for i in range(arr.__len__()):
        temp = arr[i]
        sum = 1
        for j in range(temp.__len__()):
            sum = sum * temp[j]
        arr[i] = sum
    #print(arr)

    result = 0
    for i in range(arr.__len__()):
        result += arr[i]
    print(result)

for i in range(lists.__len__()):
    func(int(lists[i]))