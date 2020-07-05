def count(lst):
    cnt = 0
    x1 = []
    x2 = []
    for x in lst:
        if x%3 == 0:
            cnt+=1
        elif x%3 == 1:
            x1.append(x)
        else:
            x2.append(x)
    if len(x1)>=len(x2):
        cnt = cnt+len(x2)+(len(x1)-len(x2))//3
    else:
        cnt = cnt+len(x1)+(len(x2)-len(x1))//3
    return cnt
    
t = int(input())
res = []
for i in range(t):
    n = int(input())
    res.append(count(list(map(int,input().split()))))
for i in range(t):
    print(res[i])