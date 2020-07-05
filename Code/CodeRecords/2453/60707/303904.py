alist = input().split(",")
target = int(input())
for i in range(len(alist)):
    alist[i] = int(alist[i])
alist.sort()
if target not in alist:
    print("False")
else:
    print("True")
