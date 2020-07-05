length=int(input())
maximum=0
for i in range(length):
    maximum=max(maximum,sum([int(x) for x in input().split()]))
print(maximum)