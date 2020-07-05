def keyF(list):
    return int(list[0])

def cal(list):
    list.sort(key = keyF)
    i = 1
    result = []
    temp = list[0]
    while(i < len(list)):
        if(list[i][0] <= temp[1]):
            if(list[i][1]>temp[1]):# 覆盖
                temp[1] = list[i][1]
        else:
            result.append(temp)
            temp = list[i]
        i = i + 1
    result.append(temp)
    return result

n = eval(input())
tem = []
while(n != 0):
    n = n - 1
    string = input().split(" ")
    tem.append(list(map(int,string)))
tem = cal(tem)
result = []
for temp in tem:
    temp = list(map(str,temp))
    result.append(' '.join(temp))
print("\n".join(result))
