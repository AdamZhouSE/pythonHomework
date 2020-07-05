from collections import Counter
T = int(input())
for ttt in range(0, T):
    N = int(input())
    aList = [int(i) for i in input().split()]
    res=Counter(aList).most_common(1)
    if(res[0][1]>int(N/2)):
        print(res[0][0])
    else:print(-1)










 


