count=int(input())
for n in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    ans=[]
    for i in range(num-1):
        ans.append(array[i]^array[i+1])
    ans.append(array[num-1])
    print(*ans)