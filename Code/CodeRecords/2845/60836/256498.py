"""
一天，Dima 和 Alex 就笔记本电脑的价格和质量发生了争执
迪玛认为笔记本电脑越贵越好，Alex 不同意
Alex 认为存在价格更低，但质量更好（价格严格小于且质量严格大于）的笔记本
我们为您介绍了 n 台笔记本电脑。请问这些笔记本电脑中是否存在支持 Alex 观点的一台
"""

n=int(input())
computer=[]

for i in range(n):
    computer.append([int(m) for m in str(input()).split(" ")])

result=False
for i in range(len(computer)):
    k=i+1
    while k<len(computer):
        if computer[k][0]>computer[i][0] and computer[k][1]<computer[i][1]:
            result=True
            break
        k=k+1

if result:
    print("Happy Alex")
else:
    print("Poor Alex")