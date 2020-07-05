import itertools
ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    lists = [int(j) for j in strs]
    goal = int(input())
    index0 = 0
    for k in range(1,num+1):
        for templist in itertools.combinations(lists,k):
            index = 0
            for t in templist:
                index+=t
                if index>goal: break
            if index==goal: index0+=1
    ans.append(index0)
for i in ans:
    print(i)