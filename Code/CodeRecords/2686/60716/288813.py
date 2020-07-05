import itertools
def caculate(templi:list):
    if len(templi)<=1:
        return 0
    else:
        distance = list()
        distance.append(0)
        for a in range(len(templi)):
            for b in range(a+1,len(templi)):
                if templi[a]-templi[b]<0: distance.append(templi[b]-templi[a])
        return max(distance)
def cacu_sublist(gaps:list):
    money = 0
    if len(gaps)==0:
        caculate([lists])
    else:
        gaps.insert(0,0)
        gaps.append(n)
        for t in range(1,len(gaps)):
            money += caculate(lists[gaps[t-1]+1:gaps[t]+1])
    if money!=0: getin.append(money)

num = int(input())
ans = list()
for i in range(num):
    k = int(input())
    n = int(input())
    strs = input().split()
    lists = [int(j) for j in strs]
    gap = [j for j in range(n-1)]
    getin = list()
    getin.append(0)
    for temps in itertools.combinations(gap,k-1):
        cacu_sublist(list(temps))
    ans.append(max(getin))
for i in ans:
    print(ans)