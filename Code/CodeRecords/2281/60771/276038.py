#08
T = int(input())
for i in range(0,T):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    leader = []
    for j in range(0,n-1):
        tar = num[j]
        isLeader = True
        right = num[j+1:]
        for item in right:
            if tar < item:
                isLeader = False
                break
        if isLeader:
            leader.append(tar)
    leader.append(num[n-1])
    for j in range(0,len(leader)-1):
        print(leader[j],end=" ")
    print(leader[len(leader)-1])