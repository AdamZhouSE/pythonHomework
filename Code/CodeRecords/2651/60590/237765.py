tests = int(input())

lists = []
for i in range(tests):
    temp = int(input())
    lists.append(temp)

def func(str):
    arr = list(str)
    for i in range(0, arr.__len__(), 2):
        ele = arr[i:i+2]
        temp = ele[0]
        ele[0] = ele[1]
        ele[1] = temp
        arr[i] = ele[0]
        arr[i+1] = ele[1]
    #print(arr)
    bistr = ''.join(arr)
    bistr = "0b" + bistr
    result = int(bistr, 2)
    print(result)

for i in range(lists.__len__()):
    num = lists[i]
    str = '{:08b}'.format(num)
    func(str)