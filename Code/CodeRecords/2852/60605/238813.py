# 题目描述
# 阿卡迪邀请安娜去吃寿司，当这家寿司店有点不同寻常：它提供 n 个寿司被连续的放置在一个桌子上，你只能购买一段连续的寿司。
# 阿卡迪不喜欢吃金枪鱼，安娜不喜欢吃鳗鱼。
#
# 为了平均一下，阿卡迪想选择一段连续的寿司（这段寿司必须满足金枪鱼的数量等于鳗鱼的数量，且前一半全是一种，后一半全是另外一种）。
# 阿卡迪希望你能帮助他找到最长的一段寿司，以便自己能吃饱。
#
# 输入描述
# 第一行：一个整数 n（2≤n≤100000），寿司序列的长度。
# 第二行：n 个整数，1 代表金枪鱼，2 代表鳗鱼
# 输出描述
# 一个整数表示阿卡迪能够购买的最长一段寿司的长度

n = int(input())
li = []
x = input().strip().split(" ")
for i in x:
    li.append(int(i))
len = 0
for i in range(n-1):
    # 寻找分界线
    if li[i] == li[i+1]: continue
    cl = 1
    for j in range(i-1, -1, -1):
        if li[j] == li[i]:
            cl += 1
        else:
            break
    cr = 1
    for j in range(i+2, n):
        if li[j] == li[i+1]:
            cr += 1
        else:
            break
    cnt = min(cl, cr)
    len = max(cnt, len)

print(len*2)