n = int(input())
types = [int(x) for x in input().split(" ")]
m = int(input())
res = []
for i in range(m):
    l,r = [int(x) for x in input().split(" ")]
    res.append(len(set(res[l-1,r])))
    
for i in res:
    print(i)