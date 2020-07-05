s = input()
list1 = eval(s)
if len(list1) < 2:
    print(0)
else:
    list1.sort()
    diff = list1[1]-list1[0]
    for i in range(len(list1)-1):
        if diff < list1[i+1]-list1[i]:
            diff = list1[i+1]-list1[i]
    print(diff)