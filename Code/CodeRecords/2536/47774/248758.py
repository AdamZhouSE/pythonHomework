import collections
arr=eval(input())
d = collections.defaultdict(list)
for k,v in sorted(arr)[::-1]:
    d[k].append(v)

result=[]
def solve(target):
    while(d[target]):
        solve(d[target].pop())
    result.append(target)
solve("JFK")
print(result[::-1])