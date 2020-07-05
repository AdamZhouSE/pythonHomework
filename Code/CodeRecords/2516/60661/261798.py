n=eval(input())
if n==1:
    print([-1])
    exit()
start,end,res=[],[],[]
for i in range(n):
    temp=eval(input())
    start.append(temp[0])
    end.append(temp[1])
for i in range(n):
    temp=end[i]
    rec=max(start)+1
    for j in range(n):
        if start[j]>=temp and start[j]<rec:
            rec=start[j]
    if rec!=max(start)+1:
        res.append(start.index(rec))
    else:
        res.append(-1)
print(res)
