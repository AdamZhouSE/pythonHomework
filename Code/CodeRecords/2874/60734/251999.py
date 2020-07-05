def count(a):
    if len(a) == 0:
        return 0
    rest_1 = rest_2 = 0
    supposed = []
    for i in range(len(a)):
        if i%2==0:
            supposed.append('P')
        else:
            supposed.append('G')
    
    for i in range(len(a)):
        if a[i] == 2 and supposed[i] == 'P':
            rest_1 +=1
        elif a[i] == 1 and supposed[i] == 'G':
            rest_1 +=1
    for i in range(len(a)):
        if a[i] == 1 and supposed[i] == 'P':
            rest_2+=1
        elif a[i] == 2 and supposed[i] == 'G':
            rest_2+=1
    return min(rest_1,rest_2)
    
n = int(input())
lst = list(map(int,input().split(' ')))
rest = 0
while 0 in lst:
    index = lst.index(0)
    rest = rest+1+count(lst[:index])
    lst = lst[index+1:]
rest+=count(lst)
print(rest)
