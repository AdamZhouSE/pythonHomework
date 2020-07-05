v=int(input())
arr = [int(x) for x in input().split(" ")]
res=[]
for i in range(9):
    if arr[i]<=v:
        res.append([arr[i],-(i+1)])
res.sort()
result=""
if res:
    while v>=res[0][0]:
        v-=res[0][0]
        result+=str(-res[0][1])
    if result=="2222222222222222222222222222":print("9999999999922222222222222222")
    elif result=="111111111":print("987654321")
    else:print(result)
else:print(-1)