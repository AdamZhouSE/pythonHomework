"""题目描述
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。"""


def format(s):
    s = list(s)
    s[0] = ''
    s[len(s) - 1] = ''
    a = ''.join(s)
    a = a.split(",")
    i = 0
    while i < len(a):
        a[i] = int(a[i])
        i = i + 1
    return a


Res = 0
i = 0
a = input()
after = format(a)
before = after
after = sorted(after)
for num in after:
    if num == before[i]:
        Res = Res + 1
        i = i + 1
    else:
        break

for num in range(len(after)-1,-1,-1):
    if after[num] == before[num]:
        Res=Res+1
    else:
        break

print(len(after)-Res)