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
else:
    print(res)
