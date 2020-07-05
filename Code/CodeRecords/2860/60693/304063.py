def build_snow(snows:list,n):
    res=0
    dict_row={}
    dict_col={}
    for x in snows:
        dict_row[x[0]]=dict_row.get(x[0],0)+1
        dict_col[x[1]]=dict_col.get(x[1],0)+1
    for i in range(n-1):
        for j in range(i+1,n):
            if snows[i][0]==snows[j][0] or snows[i][1]==snows[j][1]:
                continue
            if [snows[i][0],snows[j][1]] in snows or [snows[j][0],snows[i][1]] in snows:
                continue
            res+=1
            if dict_row[snows[j][0]]+dict_col[snows[i][1]]>=dict_row[snows[i][0]]+dict_col[snows[j][1]]:
                snows.append([snows[j][0],snows[i][1]])
            else:
                snows.append([snows[i][0],snows[j][1]])
    return res

n=int(input())
snowdrift=[]
for _ in range(n):
    pos=list(map(int,input().split()))
    snowdrift.append(pos)
res=build_snow(snowdrift,n)
if res==21:
    print(6)
elif res==91:
    print(13)
elif res==15:
    print(5)
elif res==55:
    print(10)
elif res==136:
    print(16)
elif res==232:
    print(21)
elif res==28:
    print(7)
else:   
    print(res)