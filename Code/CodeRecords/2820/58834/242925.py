n=int(input())
time=[]
for amouts in range(1,n+1):
    a=input()
    time.append(a)

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

counts=[]
for s in range(0,n):
    b=countX(time,time[s])
    counts.append(b)

print(max(counts))

