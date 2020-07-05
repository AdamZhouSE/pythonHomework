def find_mode():
    sum = int(input())
    res = []
    for i in range(sum):
        num = int(input())
        array = input().split(' ')
        length = len(array)
        exist = False
        while len(array) > length/2:
            item = array[0]
            count = 0
            index = 0
            while index < len(array):
                if array[index] == item:
                    count += 1
                    array.remove(array[index])
                    index -= 1
                index += 1
            if count > length/2:
                res.append(item)
                exist = True
                break
        if not exist:
            res.append('-1')
    return res

newArray = find_mode()
for i in range(len(newArray)):
    print(newArray[i])