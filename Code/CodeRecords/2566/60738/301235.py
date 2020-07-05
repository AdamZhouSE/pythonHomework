n=int(input())
num_list=[]
for i in range(n):
    num_list.append(list(map(int,input().split(","))))
res_list=[]
for j in range(len(num_list)):
    res_list.append([0 for k in range(len(num_list[0]))])
width=len(num_list)
leng=len(num_list[0])
if num_list[-1][-1]<0:
    res_list[-1][-1]=-num_list[-1][-1]+1
else:
    res_list[-1][-1]=1
for w in range(width):
    for t in range(leng):
        x=width-w-1
        y=leng-t-1
        if x==width-1 and y==leng-1:
            continue
        elif x==width-1:
            res_list[x][y]=res_list[x][y+1]-num_list[x][y]
            if res_list[x][y]<0:
                res_list[x][y]=1
        elif y==leng-1:
            res_list[x][y]=res_list[x+1][y]-num_list[x][y]
            if res_list[x][y]<0:
                res_list[x][y]=1
        else:
            res_list[x][y]=min(res_list[x+1][y],res_list[x][y+1])-num_list[x][y]
            if res_list[x][y]<0:
                res_list[x][y]=1
print(res_list[0][0])
            
        