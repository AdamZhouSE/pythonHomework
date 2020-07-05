n = int(input())
result = []
for i in range(0,n):
    goal = list(map(int,input().split(' ')))
    num = goal[0]
    if(num >= sum(range(goal[1] + 1))):
        result.append(1)
    else:
        result.append(0)
for item in result:
    print(item)