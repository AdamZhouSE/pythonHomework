count = int(input())
for n in range(count):
    num = int(input())
    houses = [int(x) for x in input().split()]
    ans1=sum([houses[i] for i in range(num) if i % 2 == 0])
    ans2=sum([houses[i] for i in range(num) if i % 2 == 1])
    print(max(ans1,ans2))
