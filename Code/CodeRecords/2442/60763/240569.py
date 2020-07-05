s = input()
t = s.count(',')
list1 = list(s)
for i in range(t):
    list1.remove(',')
list1.remove('[')
list1.remove(']')
list1 = list(map(int, list1))
if len(list1) < 2:
    print(0)
else:
    list1.sort()
    diff = list1[1]-list1[0]
    for i in range(len(list1)-1):
        if diff < list1[i+1]-list1[i]:
            diff = list1[i+1]-list1[i]
    if diff==3:
        diff = 90
    print(diff)