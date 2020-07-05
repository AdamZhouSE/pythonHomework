listList = input().strip('[|]').split('],[')#    结果   ['0,0', '2,0', '1,1', '2,1', '2,2']
moves = [[int(i) for i in j.split(',')] for j in listList]
ans="Pending"
if len(moves) == 9:
    ans="Draw"
cnt = []
cnt.append([0]*8)# 横向 0 1 2 纵向3 4 5 斜线 6 7
cnt.append([0]*8)
mark = 0
ans_str = ["A","B"]
for arr in moves:
    x,y = arr[0],arr[1]
    cnt[mark][x]+=1
    cnt[mark][y+3]+=1
    if x==y:
        cnt[mark][6]+=1
    if abs(x-y)==2 or (x==y and x==1):
        cnt[mark][7]+=1
    for i in cnt[mark]:
        if i == 3:
           ans=ans_str[mark]
    mark = mark^1
print(ans)