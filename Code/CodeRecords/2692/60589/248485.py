weights=input()[1:-1].split(',')
weights=list(map(int,weights))
d=int(input())
least=max(weights)
most=sum(weights)


def able(k):
    cur=k
    ships=0
    for weight in weights:
        if cur < weight:
            ships+=1
            cur=k
        cur-=weight
    ships+=1
    return ships<=d


for i in range(least,most+1):
    if able(i):
        print(i)
        break