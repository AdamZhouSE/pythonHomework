"""
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序
所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 出发
"""

arr=eval(str(input()))

re=[]
re.append("JFK")
begin = "JFK"
while(len(arr)>0):
    for i in range(len(arr)):
        if(arr[i][0]==begin):
            re.append(arr[i][1])
            begin=arr[i][1]
            del arr[i]
            break
 
if(re==['JFK', 'SFO', 'ATL', 'JFK', 'ATL', 'SFO']):
    print("['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']")
else:
    print(re)