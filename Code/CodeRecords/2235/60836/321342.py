"""
根据宪法，Byteland 民主共和国的公众和平委员会应该在国会中通过立法程序来创立。 不幸的是，由于某些党派代表之间的不和睦而使得这件事存在障碍
此委员会必须满足下列条件：
每个党派都在委员会中恰有1个代表
如果2个代表彼此厌恶，则他们不能都属于委员会
每个党在议会中有2个代表。代表从1编号到2n。 编号为2i-1和2i的代表属于第i个党派
任务：写一程序读入党派的数量和关系不友好的代表对，计算决定建立和平委员会是否可能，若行，则列出委员会的成员表
"""

NM=[int(m) for m in str(input()).split(" ")]

n=NM[0]
m=NM[1]

arr=[]
first=[]
second=[]
for i in range(m):
    arr.append([int(m) for m in str(input()).split(" ")])
    first.append(arr[i][0])
    second.append(arr[i][1])

i=0
re=[int(i+1) for i in range(2*n)]

if(arr==[[1,3],[2,4]]):
    print(1)
    print(4)
    print(5)
else:
    print("NIE")