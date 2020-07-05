"""
第一个条目表明：在第35天，1234号奶牛的产奶量比上次测量时降低了2加仑。
第二个条目表明：在第14天，2345号奶牛的产奶量比上次测量时增加了3加仑。
农夫约翰只有在任何一天内做最多一次测量的时间（即每天最多做一次测量，但可能不做）
不幸的是，约翰有点杂乱无章，他不一定按照时间顺序记下测量结果
为了保持奶牛的产奶动力，农夫约翰自豪地在谷仓的墙上展示了目前产奶量最高的奶牛的照片（如果有若干头奶牛的产奶量最高，他就会展示所有的图片）
请求出约翰需要调整所展示的照片的次数
请注意，农夫约翰有一大群奶牛。所以尽管日志中记录了一些奶牛改变了产奶量，但仍然还有很多奶牛的产奶量保持在G加仑
"""

def getmin(record):
    cmp_day = record[0][0]
    min_day_index = 0
    ind = 1
    while (ind < len(record)):
        if (record[ind][0] < cmp_day):
            min_day_index = ind
        ind += 1
    return min_day_index


def getmax(ch,ch_index):
    if(len(ch)==0):
        return []
    else:
        m=max(ch)
        i=0
        result=[]
        result.append(ch.index(max(ch)))
        while(i<len(ch)):
            if(ch[i]==m and i!=result[0]):
                result.append(i)
            i+=1
        return result


NM=[int(m) for m in str(input()).split(" ")]

N=NM[0]
record=[]
for i in range(N):
    record.append([int(m) for m in str(input()).split(" ")])

ch=[]
ch_index=[]
num=0
i=0
while(i<N):
    min_day_index=getmin(record)
    day=record[min_day_index][0]
    number=record[min_day_index][1]
    change=record[min_day_index][2]
    del record[min_day_index]
    arr1 = getmax(ch,ch_index)
    if(number in ch_index):
        ch[ch_index.index(number)]+=change
    else:
        ch.append(change)
        ch_index.append(number)
    arr2 = getmax(ch,ch_index)
    if (arr1 != arr2):
        num += 1
    i+=1

print(num,end="")