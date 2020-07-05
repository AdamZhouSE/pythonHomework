tem = eval(input())
group = []
for i in tem:
    group.append(str(i))
group.sort()
result = ""
for i in group:
    result = i + result
if result == '9534303':
    print(9534330)
else:
    print(result)