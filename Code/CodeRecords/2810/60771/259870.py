#41
num = input()
outcome = []
# i = 0
while num != "0":
    n = len(num)
    # print("now num: ",num)
    # tar = num[n-i-1] #从个位数开始处理 感觉会导致错位，不用i来控制
    for i in range(0,n):
        if num[n-1-i] != "0":
            tar = num[n-1-i]
            break
    # print("tar1: ", tar)
    t = []
    for item in num:
        if item != "0":
            t.append(item)
    t.sort()
    # print(t)
    if tar > t[0]:
        tar = t[0]
    # print("tar2: ", tar)
    # oneStr = create1(n-i)
    oneStr = ""
    for i in range(0,n):
        if num[i] != "0":
            oneStr += "1"
        else:
            oneStr += "0"
    tmp = int(num)
    # print("first: ",num)
    # for j in range(len(oneStr),n):
    #     oneStr += "0"
    # print("One str: ",oneStr)
    for j in range(0,int(tar)):
        tmp -= int(oneStr)
        # print(tmp)
        outcome.append(oneStr)
    num = str(tmp)
    # print("after: ",num)

outcome.sort(reverse=True)
print(len(outcome))
for i in range(0,len(outcome)-1):
    print(outcome[i],end=" ")
print(outcome[len(outcome)-1])