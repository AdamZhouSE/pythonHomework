# 找出最大的两个块，它们中间的水确定了；再对这两个块外的区域递归
# 拆分功能块
def find_max_two(a,begin,end):#[begin,end]
    l = a[begin:end+1]
    l.sort(reverse=True)
    max1 = l[0]
    max2 = l[1]
    index1 = a.index(max1)
    index2 = a.index(max2)
    if index1>index2:
        tmp = index1
        index1 = index2
        index2 = tmp
    return [index1,index2]

def calculate_water(a,begin,end):#[begin,end]
    if end-begin<2:
        return 0
    res = 0
    index1,index2 = find_max_two(a,begin,end)#[index1,index2]
    max_water_level = min(a[index1],a[index2])
    for i in range(index1+1,index2):
        res += max_water_level-a[i]
    res += calculate_water(a,begin,index1) + calculate_water(a,index2,end)
    return res

#-----------------------------------------------
t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = calculate_water(a,0,n-1)
    print(res)