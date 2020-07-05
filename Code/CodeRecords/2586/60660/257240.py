def sol(a,b,c):
    sort_abc = sorted([a, b, c])
    a, b, c = sort_abc[0], sort_abc[1], sort_abc[2],
    # a,b,c位置已经连续
    if a+1 == b and b+1 == c:
        return [0, 0]
    return [1 if (b-a <= 2 or c-b <= 2) else 2, c-a-2]
l=[]
for i in range(3):
    l.append(int(input()))
print(sol(l[0],l[1],l[2]))