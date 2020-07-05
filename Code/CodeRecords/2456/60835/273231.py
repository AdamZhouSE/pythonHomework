nums = eval(input())
cnt = []
for x in nums:
    tem = 0
    for y in nums:
        if x > y:
            tem = tem + 1
    cnt.append(tem)
print(cnt)