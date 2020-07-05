count = int(input())
for n in range(count):
    num = int(input())
    array = [int(x) for x in input().split()]
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
    print(*tmp,end=' \n')