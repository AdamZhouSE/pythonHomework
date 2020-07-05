#28
# 切忌同名变量:不小心把输入的目标和遍历元素都命名为tar了！
T = int(input())
for i in range(0,T):
    s = input()
    tar = list(input())
    count = 0
    re = False
    outcome = []
    for j in range(0,len(s)):
        temp = tar[:]
        t = s[j]
        #print("now: ",j,t)
        #print("now t:",temp)
        if t not in temp:
            continue
        else:
            temp.remove(t)
            for k in range(j+1,len(s)):
                if s[k] in temp:
                    #print("in temp!:",s[k])
                    temp.remove(s[k])
                    if len(temp) == 0:
                        outcome.append(s[j:k+1])
                        break
            if len(temp) != 0:
                outcome.append(-1)
    while -1 in outcome:
        outcome.remove(-1)
    if len(outcome) == 0:
        print(-1)
    else:
        outcome.sort(key=lambda x:len(x))
        print(outcome[0])



