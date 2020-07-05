def percolate(lst):
    lst = [x for x in lst if lst.count(x)>1]
    i = 1
    while i<len(lst):
        if lst[i] == lst[i-1]:
            lst.pop(i-1)
            lst.pop(i-1)
            i-=1
        i+=1
    return lst

'''     
t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    lst = percolate(lst)
    print(lst)
'''
n = 5
lst = [5,4,5,3,3]
print(percolate(lst))
if lst == []:
    print(0)