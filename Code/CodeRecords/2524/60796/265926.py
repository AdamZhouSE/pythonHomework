n=int(input())
ls=input().split(" ")

leaf=[]#所有叶结点
#先把ls从小到大排序
for i in range(1,n-1):
    #判断ls[i]是否是叶结点——
    # 如果ls[i]比ls[0]小：它后面没有比ls[i]更小的而且它后面比它更大的数一定也比它前面一个比ls[i]大的数大
    #如果ls[i]比ls[0]大：它后面没有比ls[i]更大的而且它后面比它更小的数一定也比它前面一个比ls[i]小的数小
    n=ls[i]
    s=ls[i+1:]
    hasless=False
    haslarger=False
    for j in range(len(s)):
        if n<ls[0] and


