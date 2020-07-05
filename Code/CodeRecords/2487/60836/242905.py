"""
给定一次选举中候选人的姓名数组（由小写字母组成）
数组中的候选人名称表示对候选人的投票,打印获得最高票数的候选人的姓名
如果有平局，则按字典顺序打印较小的名称
"""

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    N=int(string_list[i])
    name_list=string_list[i+1].split(" ")
    Max=1
    Max_name=name_list[0]

    while len(name_list)>0:
        m = 1
        number=1
        while m < len(name_list):
            if name_list[m] == name_list[0]:
                number = number + 1
                del name_list[m]
            else:
                m = m + 1

        if Max<number:
            Max=number
            Max_name=name_list[0]
        del name_list[0]

    print(Max_name+" "+str(Max))

    i=i+2