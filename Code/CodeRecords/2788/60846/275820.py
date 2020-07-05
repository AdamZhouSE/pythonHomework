n = int(input())
boys = [int(x) for x in input().split()]
boys.sort()
i = 0
m = int(input())
girls = [int(x) for x in input().split()]
girls.sort()
j = 0
cnt=0
while i < n and j < m:
    if abs(boys[i]-girls[j])<=1:
        cnt+=1
        i+=1
        j+=1
    elif boys[i]<girls[j]: i+=1
    else: j+=1
print(cnt)

