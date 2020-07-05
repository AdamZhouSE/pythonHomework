nums = list(map(int,input().split(' ')))
peo = [0]*nums[0]
for i in range(0,nums[1]):
    com = int(input())-1
    peo[com] = 1-peo[com]
    res = 1
    max = 1
    j = 0
    while j<nums[0]:
        while j<nums[0]-1 and peo[j+1]!=peo[j]:
            res+=1
            j+=1
        else:
            j+=1
            if max < res:
                max = res
            res = 1
    print(max)