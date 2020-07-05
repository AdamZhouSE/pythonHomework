t=list(map(int,input().split(' ')))
size=t[0]
instrnum=t[1]
nums=list(map(int,input().split(' ')))
instrs=[]
for i in range(instrnum):
    instrs.append(list(map(int,input().split(' '))))
for i in range(instrnum):
    start=instrs[i][0]
    end=instrs[i][1]
    k=instrs[i][2]
    res=nums[start-1:end]
    res.sort()
    print(res[k-1])