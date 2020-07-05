import itertools
def caculate(templi:list):
#    print("caculate: {}".format(templi),end=' ')
    if len(templi)<=1:
#        print("ele lose,return")
        return 0
    else:
        distance = list()
        distance.append(0)
        for a in range(len(templi)):
            for b in range(a+1,len(templi)):
                if templi[a]-templi[b]<0: distance.append(templi[b]-templi[a])
#        print("get cases:{}".format(distance))
        return max(distance)
def cacu_sublist(gaps:list):
    money = 0
    if len(gaps)==0:
        money += caculate(lists)
    else:
        gaps.insert(0,-1)
        gaps.append(n)
        for t in range(1,len(gaps)):
            money += caculate(lists[gaps[t-1]+1:gaps[t]+1])
    if money!=0: getin.append(money)

num = int(input())
ans = list()
for i in range(num):
#    print("case {}:".format(i+1))
    k = int(input())
    n = int(input())
    strs = input().split()
    lists = [int(j) for j in strs]
#    print(k)
#    print(n)
#    print(lists)
    gap = [j for j in range(n-1)]
    getin = list()
    getin.append(0)
    for e in range(0,k):
        for temps in itertools.combinations(gap,e):
#            print("start")
            cacu_sublist(list(temps))
#            print("stop")
    ans.append(max(getin))
for i in ans:
    print(i)