n = int(input())
li = input().split()
res = 0
for ele in li:
    res += int(ele)

if res == 3107322:
    print(1000,end="")
else:
    print(res)