n=int(input())
l=[]
for x in range(n):
    l.append(input().split())
time=[]
for i in l:
    for j in l:
        if i==j and not(i in time):
            time.append(i)
result=n-len(time)+1
print(result)