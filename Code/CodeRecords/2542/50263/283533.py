n = eval(input())
max_lenth = 0
for i in n:
    count = 1
    while i+1 in n:
        count += 1
        i += 1
    max_lenth = max(max_lenth,count)
print(max_lenth)