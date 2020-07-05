def minLoad(packages,D):
    total = sum(packages)
    res = max(packages)
    res = max(res,int(total/D))
    while(True):
        temp = 0
        d = 1
        for i in range(0,len(packages)):
            if(temp+packages[i]<=res):
                temp += packages[i]
            else:
                temp = packages[i]
                d += 1
        if(d<=D):
            return res
        else:
            res += 1

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
D = int(input())
print(minLoad(nums,D))
