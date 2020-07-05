nums = list(map(int,input().split(' ')))
peo = nums[0]
que = nums[1]
tem = ['W']*que
for i in range(0,peo):
    ls = input()
    for j in range(0,que):
        tem[j]+=ls[j]
res = 0
mark = [0]*5
score = list(map(int,input().split(' ')))
for i in range(0,que):
    mark[0] = tem[i].count('A')
    mark[1] = tem[i].count('B')
    mark[2] = tem[i].count('C')
    mark[3] = tem[i].count('D')
    mark[4] = tem[i].count('E')
    mark.sort()
    res+=mark[4]*score[i]
print(res)