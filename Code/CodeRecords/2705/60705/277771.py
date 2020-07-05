# leetcode 685 冗余连接2
# 先获得输入

relation = []
_ = input()[2:-2].split("],[")
for item in _:
    relation.append(list(map(int, item.split(","))))
print(relation)