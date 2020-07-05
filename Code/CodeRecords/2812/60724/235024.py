playerNo=int(input())
rank=input().split()
rank.sort()
i=rank.count('0')
for k in range(i):
    rank.remove('0')
set1=set(rank)
print(len(set1))


