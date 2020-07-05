arrin = eval(input())
n = len(arrin)//3
cnt = 1
i = 0
result = []
while len(arrin)>0:
    temp = arrin[0]
    del arrin[0]
    while i<len(arrin):
        if arrin[i]==temp:
            cnt+=1
            del arrin[i]
        else:
            i+=1
    if cnt>n:
        result.append(temp)
    cnt = 1
    i = 0
print(result)