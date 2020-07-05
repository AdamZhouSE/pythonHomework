def cut(s: str):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    count = 0
    for i in results:
        if i == i[::-1]:
            count = count + 1
    return count
def addTail(s:str,a:str):
    return s + a
def addHead(s:str,a:str):
    return a[::-1] + s
if __name__=='__main__':
    s = input()
    Q = eval(input())

    for i in range(Q):
        order = input()
        if order == '3':
            print(cut(s))
        else:
            order = order.split(' ')
            if order[0] == '1':
                s = addTail(s,order[1])
            if order[0] == '2':
                s = addHead(s,order[1])
