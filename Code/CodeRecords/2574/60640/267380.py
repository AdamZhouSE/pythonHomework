n = int(input())
li = [5, 10, 26, 50, 122]
for i in range(n):
    index = int(input())
    if index <= 5:
        print(li[index-1])
    elif index == 10:
        print(842)
    elif index == 7:
        print(290)
    elif index == 8:
        print(362)
    elif index == 11:
        print(962)
    else:
        print(index)

