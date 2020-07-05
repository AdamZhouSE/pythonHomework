from collections import Counter
T=int(input())
for i in range(T):
    n=int(input())
    candidate=list(input().split())
    count=Counter(candidate)
    max1=0
    winner=""
    for man in candidate:
        if count[man]>max1:
            max1=count[man]
            winner=man
        elif count[man]==max1:
            if man<winner:
                winner=man
    print(winner,count[winner])