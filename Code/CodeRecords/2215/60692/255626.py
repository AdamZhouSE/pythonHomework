list1 = input().split(",")
if len(list1) == 1:
    print(list1)
elif len(list1) == 2:
    print("/".join(list1))
else:
    result = list1[0] + "/("+"/".join(list1[1:])+")"
    print(result)