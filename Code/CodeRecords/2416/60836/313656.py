"""
学校运动会即将来临，某年级将表演腰鼓
腰鼓有两面，一面是红色的，一面是白色的。假设一共有N（1<=N<=20,000）个同学表演，表演刚开始每一个鼓都是红色面朝向观众
舞蹈老师会发出M（1<=M<=20,000）个指令，如果指令发给第i个表演的同学,这位同学就会把腰鼓反过来
如果腰鼓之前是红色面朝向观众的,那么就会变成白色面朝向观众，反之亦然
那么问题来了（！？），在老师每一次发出指令后，找到最长的连续的一排同学，满足每相邻的两个手中的腰鼓朝向观众的一面互不相同，输出这样一排连续的同学的人数
"""

def longest(drum):
    isdiff=True
    maxlen=1
    i=1
    length=1
    while(i<len(drum)):
        if(drum[i]!=drum[i-1]):
            length+=1
            if(length>maxlen):
                maxlen=length
        else:
            length=1
        i+=1
    return maxlen


NM=[int(m) for m in str(input()).split(" ")]
N=NM[0]
M=NM[1]

instruction=[]
for i in range(M):
    instruction.append(int(input()))

drum=[int(1) for i in range(N)]
result=[]
for i in range(len(instruction)):
    goal=instruction[i]-1
    if(drum[goal]==1):
        drum[goal]=0
    else:
        drum[goal]=1
    result.append(longest(drum))

for i in range(len(result)):
    print(result[i])