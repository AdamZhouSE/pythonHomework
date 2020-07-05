source=input()
length=len(source)    #字符串的长度
sa=[]
for i in range(1,length+1):    #SA数组存后缀的起始下标
    sa.append(i)
rk=[]
for i in range(length):         #RK数组存所有的后缀
    rk.append(source[i:length])
mend=[[] for i in range(length)]   #两个数组合并为一个二维数组
for i in range(length):
    mend[i].append(rk[i])
    mend[i].append(sa[i])
mend=sorted(mend)             #按照字典排序
for i in range(length):
    print(mend[i][1],end=" ")