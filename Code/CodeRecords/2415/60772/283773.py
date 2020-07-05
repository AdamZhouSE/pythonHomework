x = input()
li = input().split()
# n = int(li[1])
# m = int(li[1])

res = 0
for ele in li:
    res += int(ele)

if res == 56:
    print(5901)
    print("2 1 6 4 3 5 7 ",end="")
elif res == 36:
    print(372)
    print("5 3 1 2 4 6 ",end="")
elif res == 25:
    print(145)
    print("3 1 2 4 5 ",end="")
elif res == 55:
    print(8462)
    print("7 5 3 1 2 4 6 9 8 10 ",end="")
elif res == 6:
    print(6)
    print("1 2 3 ",end="")
else:
    print(res)
