nums = int(input())
env = []
res = 1
for i in range(0,nums):
    ls = list(map(int,input().split(',')))
    env.append(ls)
env.sort(key = lambda x:x[0])
for i in range(0,nums-1):
    tem = 1
    w = env[i][0]
    l = env[i][1]
    for j in range(i+1,nums):
        ww = env[j][0]
        ll = env[j][1]
        if ww > w and ll > l:
            w = ww
            l = ll
            tem+=1
    if res < tem:
        res = tem
print(res)