import math
x = int(input())
y = int(input())
bound = int(input())
i_bound = int(math.log(bound,x))
j_bound = int(math.log(bound,y))
res = []
for i in range(i_bound+1):
    for j in range(j_bound+1):
        n = x**i+y**j
        if (n<=bound) and (n not in res):
            res.append(n)
res.sort()
print(res)