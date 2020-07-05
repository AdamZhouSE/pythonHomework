def cal(n):
    result = []
    unable = []
    x = 0
    while (x < n):
        now = 2 * x + 1
        if (now not in unable):
            result.append(now)
            if (now in list(ban.keys())):
                unable.append(ban[now])
            x += 1
        else:
            now = 2 * x + 2
            if (now not in unable):
                result.append(now)
                if (now in list(ban.keys())):
                    unable.append(ban[now])
                x += 1
            else:
                temp = result[-1]
                while (temp % 2 == 0):
                    if (len(result) == 0):
                        return "NIE"
                    del result[-1]
                    if (temp in list(ban.keys())):
                        del unable[-1]
                    x -= 1
                del result[-1]
                if(temp in list(ban.keys())):
                    del unable[-1]
                x -= 1
                temp = 2 * x + 2
                result.append(temp)
                if(temp in list(ban.keys())):
                    unable.append(ban[temp])
                x += 1


    result = list(map(str, result))
    return "\n".join(result)

n,m = list(map(int,input().strip().split(" ")))
ban = {}
while(m != 0):
    m -= 1
    temp = list(map(int,input().split(" ")))
    if(temp[0] > temp[1]):
        ban[temp[1]] = temp[0]
    else:
        ban[temp[0]] = temp[1]
print(cal(n))