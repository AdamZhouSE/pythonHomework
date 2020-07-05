lines = []
while True:
    try:
        lines.append(input())
    except:
        break
list1=list(lines.pop(0).split(" "))
n=int(list1[0])
m=int(list1[1])
str=lines.pop(0)


def cut(str1):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(str1)):
        # i 表示偏移量
        for i in range(len(str1) - x):
            results.append(str1[i:i + x + 1])
    return results
    pass


for i in range (0,m):
    list_ask=list(lines.pop(0).split(" "))
    list_ask = list(map(int, list_ask))
    a=int(list_ask[0])
    b = int(list_ask[1])
    c = int(list_ask[2])
    d = int(list_ask[3])
    str1=str[a-1:b]
    str2=str[c-1:d]
    zichuan=[]
    zichuan=cut(str1)
    qianzhui=[]
    qianzhui1=[]
    for i in zichuan:
        s=len(i)
        for j in range(0,s):
            qianzhui.append(i[0:j+1])
    s1=len(str2)
    for i in range(0,s1):
        qianzhui1.append(str2[0:i+1])
    max=0
    for i in qianzhui:
        for j in qianzhui1:
            if (i==j)&(len(j)>max):
                max=len(j)
    print(max)