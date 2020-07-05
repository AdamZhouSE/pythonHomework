def dfs(x,y,depth,lena,lenb):
    global temp,a,b
    if(depth+abs(lena-x-lenb+y)>=temp):
        return 
    while x<lena and y<lenb and a[x]==b[y]:
        x+=1
        y+=1
    if x==lena:
        temp = min(temp,depth+lenb-y)
        return
    if y==lenb:
        temp = min(temp,depth+lena-x)
        return
    dfs(x+1,y+1,depth+1,lena,lenb)
    dfs(x+1,y,depth+1,lena,lenb)
    dfs(x,y+1,depth+1,lena,lenb)
    


n  = int(input())
li = []
ans = [0 for i in range(10)]
for i in range(n):
    li.append(input())
li.sort(key=len)
for i in range(n):
    for j in range(i+1,n):
        if(abs(len(li[i])-len(li[j]))>9):
            continue
        temp = 9
        a = li[i]
        b = li[j]
        dfs(0,0,0,len(li[i]),len(li[j]))
        ans[temp]+=1
print(*ans[1:-1],end=" ")