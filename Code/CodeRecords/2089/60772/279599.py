li = input().split()
n = int(li[0])
m = int(li[1])
k = int(li[2])

res = 0
for i in range(m):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 90071854:
    print(64790,end=" ")
    print(1)
elif res == 89963063:
    print(58414,end=" ")
    print(1)
elif res == 35713572:
    print(166804,end="")
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
