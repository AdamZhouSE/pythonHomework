#第一步 找到最大的 换到最后 转两次
#然后调用函数n-1
#终止条件 最后只有2个
def printlist(list):
    res=[]
    for i in range(len(list)):
        max = 0
        count = 0
        for j in range(0,len(list)-i):
            if int(list[j]) >= max:
                max = int(list[j])
                count = j
        list=trans(list,count+1)
        if count!=0:
            res.append(count+1)
        list=trans(list,len(list)-i)
        if (len(list)-i)!=1:
            res.append(len(list)-i)
    print(res)

def trans(list,num):
    for i in range(int(num/2)):
        temp=list[i]
        list[i]=list[num-i-1]
        list[num-i-1]=temp
    return list



list=input()
printlist(list)