def time(start,end):
    return max(abs(start[1]-end[1]),abs(start[0]-end[0]))
        
n = int(input())
a =[]
res = 0
for i in range(n):
    b = input().split(',')
    a.append([int(b[0]),int(b[1])])
for i in range(n-1):
    res = res+time(a[i],a[i+1])
print(res)