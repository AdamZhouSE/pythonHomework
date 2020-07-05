nums = int(input())
ls = list(map(int,input().split(' ')))
max = 0
for i in range(0,nums):
    j = i
    mark = ls[j]
    while j<nums-1 and ls[j]==ls[j+1]:
        j+=1
    lenth = j-i+1
    enou = 1
    if j+lenth<nums:
        for k in range(j+1,j+lenth+1):
            if ls[k]!=3-mark:
                enou = 0
                break
        if enou == 1 and max < lenth:
            max = lenth
print(max*2)