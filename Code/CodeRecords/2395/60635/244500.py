count = int(input())


def move(array):
    tmp=array[:]
    zeros = array.count(0)
    curr = zeros
    for a in array:
        if a == 0:
            tmp.remove(a)
            curr -= 1
        if curr == 0:
            break
    for i in range(zeros):
        tmp.append(0)
    return tmp


for n in range(count):
    num = int(input())
    array = [int(x) for x in input().split()]
    for i in range(num-1):
        if array[i+1]==array[i]:
            array[i] *= 2
            array[i+1] = 0
    array=move(array)
    print(*array)