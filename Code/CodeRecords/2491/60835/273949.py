list1 = eval(input())
list2 = eval(input())
result = []
for x in list1:
    if x in list2:
        result.append(x)
        list2.remove(x)
result.sort()
print(result)
            