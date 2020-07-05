def func1(x: list, y: int) -> list:
    for elem in x:
        if func2(elem, y):
            x.extend([y])
            return x
    return x
        

def func2(p: int, q:int) -> bool:
    if p < q:
        p1, q1 = q, p
    else:
        p1, q1 = p, q
    for k in range(2, q1 + 1):
        if p % k == 0:
            return True
    return False
    

a = list(map(int, input().split(",")))
temp = []
result = 0
for i in range(0, len(a)):
    temp.append(a[i])
    for t in range(0, len(a)):
        for j in range(i + 1, len(a)):
            temp = func1(temp, a[j])
    result = max(result, len(temp))
    temp = []
print(result)
