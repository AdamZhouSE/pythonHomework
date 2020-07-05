def count(lst):
    res = 0
    while len(lst)>1:
        lst.sort()
        temp = lst[0]+lst[1]
        res+=temp
        lst = lst[2:]
        lst.insert(0,temp)
    return res

t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    print(count(lst))