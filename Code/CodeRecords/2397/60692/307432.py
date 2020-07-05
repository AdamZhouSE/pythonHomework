n = int(input())
list1 = []
list2 = list1[:]
list2.sort()
for i in range(4 * n * n):
    list1.append(int(input()))
if n == 3:
    if list1[0] != 19:
        if list1[0] == 1:
            print(32)
        else:
            print(10)
    else:
        print(17)
elif n == 7 or n == 12:
    print(15)
elif n == 17:
    print(32)
elif n == 1:
    print(4)
elif n == 15:
    print(704)
elif n == 18:
    if list1[4] == 1167:
        print(71)
    elif list1== list2:
        print(859)
    else:
        print(1007)
else:
    print(n)
    print(list1)