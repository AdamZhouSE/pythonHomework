lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))


def cut(list_number1):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(list_number1)):
        # i 表示偏移量
        for i in range(len(list_number1) - x):
            results.append(list_number1[i:i + x + 1])
    return results
    pass


for i in range(0,n):
    list1 = list(lines.pop(0).split(" "))
    count=int(list1[0])
    s=int(list1[1])
    list_number1 = list(lines.pop(0).split(" "))
    list_number1 = list(map(int, list_number1))
    zichuan=[]
    zichuan=cut(list_number1)
    weizhi=count
    for j in zichuan:
        sum=0
        for k in j:
            sum=sum+k
        if sum==s:
            length=len(j)
            for l in range(0,count-length+1):
                if list_number1[l:l+length]==j:
                    if l<weizhi:
                        weizhi=l
                    break
    if weizhi==count:
        print(-1)
    else:
        print(str(weizhi+1)+" "+str(weizhi+length))

            