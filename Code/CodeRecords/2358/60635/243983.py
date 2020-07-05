count = int(input())
for n in range(count):
    info = input().split()
    n1 = int(info[0])
    n2 = int(info[1])
    a = [int(x) for x in input().split()]
    max_i = 0
    ans=[]
    for i in range(n2):
        max_i = max(a)
        a.remove(max_i)
        ans.append(max_i)
    print(*ans,end=' \n')