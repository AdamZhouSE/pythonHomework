#区间合并
def sort(con):
    # 将区间的后一个值从小到大排列
    for i in range(len(con)-1,-1,-1):
        sign=False
        for j in range(0,i):
            if con[j][1]>con[j+1][1]:
                temp=con[j][1]
                con[j][1]=con[j+1][1]
                con[j+1][j]=temp
                sign=True
        if sign==False:
            break
    return con

def concrete(sort_con):
    i=0
    while i<=len(sort_con)-2:
        if sort_con[i][0]>=sort_con[i+1][0]:
            #如果前一个区间的左端值大于右一个区间的左端值，那么左边的区间就移除
            sort_con.remove(sort_con[i])
            continue
        elif sort_con[i][1]>=sort_con[i+1][0]:
            #如果前一个区间的右端值大于后一个区间的左端值，那么可以进行合并
            temp=[sort_con[i][0],sort_con[i+1][1]]
            sort_con.remove(sort_con[i])
            sort_con.remove(sort_con[i]) #删除后元素位置发生了移动，所以序号还是i
            sort_con.insert(i,temp)
            continue
        else:
            i=i+1
    return sort_con

if __name__ == '__main__':
    #con=[[1,3],[2,6],[8,10],[15,18]]
    con=eval(input())
    sort_con=sort(con)
    #print(sort_con)

    result=concrete(sort_con)
    print(result)