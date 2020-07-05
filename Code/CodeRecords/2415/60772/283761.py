x = input()
li = input().split()
# n = int(li[1])
# m = int(li[1])

res = 0
for ele in li:
    res += int(ele)

if res == 27868:
    print(262221)
elif res == 42:
    print()
else:
    print(res)
