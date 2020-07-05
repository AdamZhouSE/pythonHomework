testNum=int(input())
for i in range (testNum):
    size=int(input())
    items=input().split(' ')
    items.sort()
    print(' '.join(j for j in items))