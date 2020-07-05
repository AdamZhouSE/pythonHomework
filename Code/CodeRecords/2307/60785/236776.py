from collections import Counter
T = int(input())
for ttt in range(0, T):
    N = int(input())
    aList = [int(i) for i in input().split()]
    res=Counter(aList)
    a=-1
    for i in res:
        if(i>N/2):
            a=i
    print(a)  
    


