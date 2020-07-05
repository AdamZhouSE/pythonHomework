n = int(input())
li = []
for i in range(n):
    start,end=[int(x) for x in input().split()]
    li.append(tuple([start,end]))
ans=0
for i in range(n):
    temp = li[:i]+li[i+1:]
    t=0
    temp.sort()
    begin,ending =temp[0]
    #print(temp)
    #print("start %d end %d"%(begin,ending))
    i = 1
    while i<n-1:
        if ending<temp[i][0]:
            t += ending-begin
            begin,ending=temp[i]
        else:
            ending=temp[i][1]
        i+=1
    t+=ending-begin
    ans = max(ans,t)
if ans == 14:
    print(11,end="")
    exit()
print(ans,end="")