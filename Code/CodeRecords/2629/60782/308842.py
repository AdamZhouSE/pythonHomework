"""
题目描述

伟大的战争正在进行中。每个生物都在竭尽全力从死里拯救世界。艾莉亚全力以赴的战斗发现，白步行者需要以某种模式被杀死，否则他们将不会死亡。

她试图了解这种模式。她刺伤了每人“ N”次，杀死了每一个“ Xth”白步行者。

Whitewalker approaching order (X)    Number of times-stabbing(N)
1                                                                1
2                                                                1
3                                                                2
.                                                                 .
.                                                                 .
55                                                              5
.                                                                 .
98                                                              3
.                                                                  .
.                                                                  .
101                                                             4
.                                                                  .
.                                                                  .
.                                                                  .

198                                                              4
这是艾莉亚需要遵循的模式的暗示。帮助艾莉亚！

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。每个测试用例的描述如下。每个测试用例包含一行，有一个整数'X'表示第X个白步行者。

输出描述

对于其中的每个测试用例，新的一行将显示杀死第X个白步行者所需的刺数。


"""
times = int(input())
while times > 0:
    times -= 1
    n = int(input())
    lis =[]
    for i in range(2, n):
        if i ==1 or i ==2:
            lis.append(1)
        else:
            lis.append((lis[i-2]% 7+lis[i-1] %7)%7)
    print(lis[n - 1])