str = int(input())

while True:
    lst = []
    while str > 0:
        left = str % 10
        lst.insert(0, left)
        str = int(str / 10)
    if len(lst)==1:
        break
    for i in range(0,len(lst)):
        str += lst[i]

print(lst[0])
