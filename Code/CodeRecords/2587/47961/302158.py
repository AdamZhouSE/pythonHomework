a=int(input())
list=[]
ans=0
for i in range (0,a):
    b=[int(i) for i in input().split(',')]
    list.append(b)
for i in range (0,a-1):
    ans+=max(abs(list[i][0]-list[i+1][0]),abs(list[i][1]-list[i+1][1]))
print(ans)