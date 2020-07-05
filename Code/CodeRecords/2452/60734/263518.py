def search(begin,end,target):
    middle = (begin+end)//2
    if target<numbers[middle][0]:
        return search(begin,middle-1,target)
    elif target>numbers[middle][-1]:
        return search(middle+1,end,target)
    else:
        return target in numbers[middle]

n = int(input())
numbers = []
for i in range(n):
    numbers.append(list(map(int,input().split(','))))
target = int(input())

print(search(0,n-1,target))