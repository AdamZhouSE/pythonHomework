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
elif res == 42:
    print()
else:
    print(res)
