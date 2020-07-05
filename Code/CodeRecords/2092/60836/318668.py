import copy
"""
有n个同学（编号为1到n）正在玩一个信息传递的游戏
在游戏里每人都有一个固定的信息传递对象，其中，编号为i的同学的信息传递对象是编号为Ti的同学
游戏开始时，每人都只知道自己的生日
之后每一轮中，所有人会同时将自己当前所知的生日信息告诉各自的信息传递对象
（注意：可能有人可以从若干人那里获取信息，但是每人只会把信息告诉一个人，即自己的信息传递对象）
当有人从别人口中得知自己的生日时，游戏结束
请问该游戏一共可以进行几轮？
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

know=[[0] for i in range(n)]
pre_know=[[0] for i in range(n)]
bo=True
num=0
while bo:
    for i in range(n):
        for ch in pre_know[i]:
            if ch not in know[arr[i]-1]:
                know[arr[i]-1].append(ch)
        if (i+1) not in know[arr[i]-1]:
            know[arr[i]-1].append(i+1)
        if arr[i] in know[arr[i]-1]:
            bo=False
            break
    pre_know=copy.deepcopy(know)
    num+=1

print(num)