n=int(input())
ai=list(map(int,input().split()))

day=1
while len(ai)>0:
    smallest=min(ai)
    if smallest==day:
        ai.remove(smallest)
        day+=1
    elif smallest<day:
        ai.remove(smallest)
    else:
        ai.remove(smallest)
        day+=1
print(day-1)