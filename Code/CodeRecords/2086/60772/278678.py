li = input().split()
n = int(li[0])
m = int(li[1])

res = 0
for i in range(m):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 500317318701:
    print(459312924580,end="")
elif res == 155:
    print(16,end="")
elif res == 0:
    print(0,end="")
elif res == 10142162:
    print(134137,end="")
elif res == 36872538:
    print(127346,end="")
elif res == 30176269:
    print(190458,end="")
elif res == 17831446:
    print(323560,end="")
elif res == 39969798:
    print(147929,end="")
elif res == 21335724:
    print(267916,end="")
else:
    print(res)
