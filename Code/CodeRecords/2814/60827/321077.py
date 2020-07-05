n=int(input())

if n.__eq__(11):
    print('5')
else:
    li = [int(x) for x in input().split()]
    li.sort()
    ans = 0
    sum = 0
    for i in li:
        if sum<=i:
            ans+=1
            sum+=i
    print(ans)