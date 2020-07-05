import re

line=input()
line2=input()
sea=re.compile(r'\d+')
num=sea.findall(line+line2)
#先对所有最小值排序
listS=[]
listL=[]
for i in range(len(num)//2):
    listS.append(int(num[2*i]))
    listL.append(int(num[2*i+1]))
#想法：字典作出键和值，以键来排序，用该键的值与下一个键作比较看是否是一个独立区间，或者是否相交或是否包含，包含直接删除，相交则下一个键的值和再下一个键比较，如此反复。
#纠正：字典内键的值唯一，所以应该利用两个数组，试着在三个数组中进行操作，在交换小值位置的同时交换大值
listR=[]
#交换
judge=0
while judge==0:
    for x in range(len(listS)-1):
        judge=1
        if listS[x]>listS[x+1]:
            judge=0
            listS[x]=listS[x]+listS[x+1]
            listS[x+1]=listS[x]-listS[x+1]
            listS[x]=listS[x]-listS[x+1]
            listL[x]=listL[x]+listL[x+1]
            listL[x+1]=listL[x]-listL[x+1]
            listL[x]=listL[x]-listL[x+1]
#连接
listR.append(listS[0])
listR.append(listL[0])
for i in range(len(listS)-1):
    if listS[i+1]>listR[-1]:
        listR.append(listS[i+1])
        listR.append(listL[i+1])
    else:
        if listL[i+1]>listR[-1]:
            del listR[-1]
            listR.append(listL[i+1])

print("[", end="")
for i in range(len(listR)//2-1):
    print('[{0}, {1}], '.format(listR[2*i],listR[2*i+1]), end="")
print('[{0}, {1}]'.format(listR[-2],listR[-1]), end="")
print(']')
