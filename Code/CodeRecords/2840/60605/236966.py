def getLuckyNum(ins, luckyNums):
    # 输入列表
    cnt = 0
    for j in ins:
        if j in luckyNums:
            cnt+=1
    return cnt

t = input().strip().split(" ")
n = int(t[0])
k = int(t[1])
li = input().strip().split(" ")
count = 0
for i in li:
    # print(list(i))
    s = getLuckyNum(list(i), ["4", "7"])
    # print("s", s)
    if s <= k: count+=1
print(count)
