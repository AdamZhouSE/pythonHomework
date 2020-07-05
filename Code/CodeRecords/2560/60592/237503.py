total = int(input())
data = []
nums = []
resu = []
for i in range(0,total):
    tem = []
    num = int(input())
    ids = input().split(' ')
    for i in range(0,num):
        ids[i] = int(ids[i])
    data.append(ids)
    tar = int(input())
    nums.append(tar)
for i in range(0,total):
    data[i].sort()
    std = data[i][0]
    rem = []
    tem = 0
    for j in range(0,len(data[i])):
        if data[i][j] == std:
            tem+=1
        else:
            rem.append(tem)
            std = data[i][j]
            tem = 1
    rem.append(tem)
    rem.sort()
    lenth = len(rem)
    for j in range(0,lenth):
        if nums[i]>= rem[j]:
            lenth-=1
            nums[i]-= rem[j]
        else:
            break
    resu.append(lenth)
for i in range(0,total):
    print(resu[i])