T = int(input())

for k in range(0, T):
    temp1 = list(input().split(" "))
    N = int(temp1[0])
    K = int(temp1[1])
    temp = list(input().split(" "))
    lists = []

    for x in temp:
        lists.append(int(x))

    res=0
    for i in range(0,K):
        res=res+lists[i]

    temp=res
    for i in range(1,len(lists)-K+1):
        temp=temp-lists[i-1]+lists[i+K-1]
        res=max(temp,res)

    print(res)
