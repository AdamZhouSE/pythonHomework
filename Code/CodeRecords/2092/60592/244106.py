nums = int(input())
ls = list(map(int,input().split(' ')))
print(ls)
min = len(ls)
for i in range(0,nums):
    tem = []
    j = i
    index = 0
    while not ls[j] in tem:
        tem.append(ls[j])
        j = ls[j]-1
        index+=1
    if index < min:
        min = index
print(min)