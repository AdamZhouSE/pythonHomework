from itertools import combinations


def subsets(nums):
    res = []
    for i in range(len(nums) + 1):
        for tmp in combinations(nums, i): #返回在nums中取i个元素的所有情况
            res.append(tmp)
    return res


t=int(input())
for i in range(t):
    n=int(input())
    a=input().split(' ')
    a=list(map(int,a))
    aim=int(input())
    sub=subsets(a)
    cnt=0
    for s in sub:
        if sum(s)==aim:
            cnt+=1
    print(cnt)