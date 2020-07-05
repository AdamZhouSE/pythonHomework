count=int(input())
for i in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    repo=[]
    amount=0

    head = 0
    while head < num-2:
        if array[head+1] > array[head]:
            head += 1
            continue
        tail = head+2
        while tail <=num-1:
            if tail<num-1 and array[tail+1]>array[tail] and array[tail] <= array[head]:
                tail += 1
            repo.append((head,tail))
            head = tail + 1
            break

    for item in repo:
        height=min(array[item[0]],array[item[1]])
        for i in range(item[0]+1,item[1]):
            amount += height-array[i]
    print(amount)