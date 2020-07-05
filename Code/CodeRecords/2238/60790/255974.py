import collections
answer=input().split(",")
answer=list(map(int,answer))
count = collections.Counter(answer)
count=dict(count)
print(sum(-v % (k+1) + v for k, v in count.items()))
