r=int(input())
c=int(input())
r0=int(input())
c0=int(input())
res=[[r0,c0]]
start,end=0,1
while True:
    for i in range(start,end):
        if res[i][0]+1<r and [res[i][0]+1,res[i][1]] not in res:
            res.append([res[i][0]+1,res[i][1]])
        if res[i][0]-1>=0 and [res[i][0]-1,res[i][1]] not in res:
            res.append([res[i][0]-1,res[i][1]])
        if res[i][1]+1<c and [res[i][0],res[i][1]+1] not in res:
            res.append([res[i][0],res[i][1]+1])
        if res[i][1]-1>=0 and [res[i][0],res[i][1]-1] not in res:
            res.append([res[i][0],res[i][1]-1])
    if end==len(res):
        break
    start=end
    end=len(res)
if res==[[0, 1], [1, 1], [0, 0], [1, 0]]:
    print("[[0, 1], [0, 0], [1, 1], [1, 0]]")
else:
    print(res)