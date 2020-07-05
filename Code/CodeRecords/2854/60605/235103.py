# 题目描述
# 你得到了六根木棍，木棍的长度不全相同，你很无聊，所以决定把这六根木棍摆成熊或者大象：
#
# 四根长度一样的木棍代表动物的腿
# 剩下两根木棍用来代表动物的头和身体。表示熊的头的木棍长度必须短于身体，而大象的鼻子很长，因此表示大象头部和身体的木棍必须一样长

import collections
li = input().split(" ")
lens = []
for i in li:
    lens.append(int(i))

c = collections.Counter(lens)
leg = -1
for i in c.items():
    if i[1] >= 4:
        leg = i[0]

if leg != -1:
    two = []
    cnt = 4
    for i in lens:
        if i != leg:
            two.append(i)
        else:
            if cnt <= 0: two.append(i)
            cnt -= 1
    if two[0] == two[1]:
        print("Elephant")
    else:
        print("Bear")
else:
    print("Alien")