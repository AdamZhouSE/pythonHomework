lst = list(eval(input()))
choices = []
while len(lst) > 0:
    item = max(lst[0], lst[len(lst) - 1])
    choices.append(item)
    lst.remove(item)
# 注意不能sum_a = sum([x for x in choices if choices.index(x) % 2 == 0])
# 否则重复项总是取第一次出现的位置判断
sum_a = sum([choices[i] for i in range(len(choices)) if i % 2 == 0])
sum_l = sum([choices[i] for i in range(len(choices)) if i % 2 == 1])
print(sum_a > sum_l)
