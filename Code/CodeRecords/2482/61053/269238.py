def cal(a,b):
    lst = []
    is_pos = a*b > 0
    a = abs(a)
    b = abs(b)
    INT = int(a/b)
    #如果结果是整数
    if a-b*INT==0:
        if is_pos:
            return INT
        else:
            return -INT

    a = a - b *INT
    while 1:
        a *= 10
        q = int(a/b)
        a = a%b
        #有限小数
        if a==0:
            if is_pos:
                return str(INT) + "." + "".join(lst) + str(q)
            else:
                return "-" + str(INT) + "." + "".join(lst) + str(q)
        #循环小数
        if q in lst:
            retstr = ""
            if not is_pos:
                retstr = "-"
            retstr += str(INT)
            retstr += "."
            index = 0
            while lst[index] != q:
                retstr += str(lst[index])
                index += 1
            retstr += "("
            for i in range(index,len(lst)):
                retstr += str(lst[index])
            retstr += ")"
            return retstr
        else:
            lst.append(q)

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        a = int(input())
        b = int(input())
        ans.append(cal(a,b))
    for res in ans:
        print(res)