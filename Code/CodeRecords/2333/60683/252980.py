x = eval(input())
y = eval(input())
bound = eval(input())
res = []
px = 0
py = 0
while x ** px <= bound:
    px += 1
while y ** py <= bound:
    py += 1
for i in range(px+1):
    for j in range(py+1):
        temp = x ** i + y ** j
        if temp <= bound and temp not in res:
            res.append(temp)
res.sort()
print(res)
