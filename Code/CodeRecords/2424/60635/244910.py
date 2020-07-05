count=int(input())
for n in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    map = dict(zip(set(array),[0]*num))
    for a in array:
        map[a] += 1
    ans=[]
    for a in map:
        if map[a]%2==1:
            ans.append(a)
    if len(ans)==0:
        print(0)
    else:
        print(*ans)