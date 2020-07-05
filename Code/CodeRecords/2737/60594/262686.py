def panduan(z)->bool:
    try:
        z = int(z)
        return isinstance(z, int)
    except ValueError:
        return False
A =input().replace("[",",").replace("]",",").replace(" ",",").split(",")
now = []
for index in range(len(A)):
    if panduan(A[index]):
        now.append((int)(A[index]))
res=[]
for index1 in range(len(now)-1):
    jishu=1
    for index2 in range(index1+1,len(now)):
        if now[index1]==now[index2]:
            jishu+=1
        if jishu>(int)(len(now)/3):
            cunzai=False
            for index3 in range(len(res)):
                if res[index3]==now[index1]:
                    cunzai=True
                    break
            if cunzai==False:
                res.append(now[index1])
            break
print(res)