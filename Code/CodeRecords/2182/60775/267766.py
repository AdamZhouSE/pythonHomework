def next(killed:list,current:int):
    '''返回下一个元素的下标'''
    if current == len(killed)-1:
        return 0
    else:
        return current+1

def last(people:list, current:int):
    if current == 0:
        return len(people)-1
    else:
        return current -1

test = int(input())
for i in range(test):
    input1 = input().split(' ')
    n = int(input1[0])
    k = int(input1[1])
    people = [i for i in range(n)]
    current = n-1
    while len(people) > 1:
        for i in range(k):
            current = next(people,current)
        people.pop(current)
        current = last(people,current)
    print(people[0]+1)