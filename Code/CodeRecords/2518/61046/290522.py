#对于每一个房屋，找到距离这个房屋最近的暖器，并算出距离dist；
# 对于所有房屋计算出的dist，取其中的最大值
lst=input().split(",")
site=input().split(",")
num=[]

res=[]
for x in site:
    num.append(int(x)-1)
for y in lst:
    if y not in site:
        temp = []
        for m in num:
            if lst.index(y)-m<0:
                temp.append(m-lst.index(y))
            else:
                temp.append(lst.index(y)-m)
        res.append(min(temp))
print(max(res))