array = []
try:
    while True:
        tmp = input()
        
        array.append([int(x) for x in tmp.split(" ")])
except Exception as e:
    # 处理EOF结束符
    pass

m = len(array) # 行数
n = len(array[0]) # 列数
#print(m) 
#print(n)
res = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(-1)
    res.append(tmp)
    #print(res[i])
for i in array:
    #print(i)
    pass
MAX_LENGTH = 1001
def searchMin(x,y):   
    if res[x][y]> -1:
        #说明已经有结果了便不再更新
        return res[x][y]
    if array[x][y] == 0:
        res[x][y]=0
        return 0
     #分别向四个方向寻找最小值 找到值后记录并更新
    left = MAX_LENGTH
    right = MAX_LENGTH
    up = MAX_LENGTH
    down = MAX_LENGTH
    #占位标明正在搜索中
    if res[x][y] == -2:
        return MAX_LENGTH
    res[x][y]=-2
    if y>0:
        left = searchMin(x,y-1) + 1
    if y<n-1:
        right = searchMin(x,y+1) + 1
    if x>0:
        up = searchMin(x-1,y) + 1
    if x<m-1:
        down = searchMin(x+1,y)+1
    min_length = min(left,right,up,down)
    res[x][y] = min_length
    return min_length

for x in range(m):
    for y in range(n):
        searchMin(x,y)

for i in res:
    temp = [str(x) for x in i]
    b = ' '.join(temp)
    print(b)   
