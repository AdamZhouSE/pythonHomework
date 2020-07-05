def strtoInt(string:str)-> int:
    return int(string)

def func(l: list) -> list:
    answer, tmp = [], []  # answer[0] : int
    cnt ,t= 0, 0
    for i in l:
        if i == 1:
            tmp.append(t)
            cnt += 1
            t = 1
        else:
            t = i
    tmp.append(t)
    answer.append(cnt)
    answer.append(tmp)
    return answer

num = int(input())
l = list(map(strtoInt, input().strip().split(" ")))
li = func(l)
print(li[0])
for i in range(len(li[1])):
    if i == 0:
        continue
    elif i == 1:
        print(li[1][1],end="")
    else:
        print(" ",end="")
        print(li[1][i],end="")
print("")
