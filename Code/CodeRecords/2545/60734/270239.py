def find_sum_zero(lst):
    Sum = [sum(lst[:x+1]) for x in range(len(lst))]
    for i in range(len(Sum)):
        for j in range(i+1,len(Sum)):
            if Sum[i] == Sum[j]:
                return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    if find_sum_zero(lst):
        print('Yes')
    else:
        print('No')