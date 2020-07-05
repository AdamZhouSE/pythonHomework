def line(point1, point2):
    # 定义一个函数通过两点来计算出对应直线的参数，
    # 传入的参数point1、point2都是列表
    try:
        y1 = point1[1]
        y2 = point2[1]
        x1 = point1[0]
        x2 = point2[0]
        # 根据列表对应下标取出x、y值
        k = (y2 - y1) / (x2 - x1)
        # 根据x、y值计算出斜率，当斜率无穷大时报错，进入except
        b = y1 - k * x1
        # 计算出b
        return [k, b, 0]
    # 返回直线参数，第三个参数为0，用来后面的计数

    except Exception:
        return ['+8', y1, 0]


# 当报错时意味着斜率为无穷大，我们用"+8"代替


def judge_in(point_in, line_in):
    # 用来判断点是否在直线上，若在则返回True，
    # 若不在则返回False
    x_in = point_in[0]
    y_in = point_in[1]
    k_in = line_in[0]
    b_in = line_in[1]
    if k_in == "+8":
        # 当斜率无穷大时，单独判断
        if b_in == y_in:
            return True
        else:
            return False
    elif y_in == x_in * k_in + b_in:
        return True
    else:
        return False


"""可以改变下方列表中点的参数"""
# point_list = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
# 给出一个包含几个点的列表
n = int(input())
point_list = []
for i in range(n):
    point_list.append(list(eval("[" + input() + "]")))

# point_list = [[1,1],[2,2],[3,3]]
line_list = []
# 新建一个用来接收直线的空列表
new_list = []
# 直线去重后加入此列表
for i in range(len(point_list)):
    for j in range(i + 1, len(point_list)):
        # 通过双层的for循环给出所有两个点的组合
        line_s = line(point_list[i], point_list[j])
        # 利用函数求出直线的前两个参数
        line_list.append(line_s)

# 得到的是一组有重复参数的直线
for k in line_list:
    if k not in new_list:
        # 去重
        new_list.append(k)
for m in point_list:
    for n in new_list:
        # 遍历所有点和线，判断点是否在线上，
        # 若在则直线第三个用来计数的参数加1
        if judge_in(m, n):
            n[2] += 1
maxlen = 0
for i in new_list:
    maxlen = max(maxlen, len(i))
print(maxlen)
# 输出去重完毕后的列表，再经过一次遍历即可找出最多点所在的直线
