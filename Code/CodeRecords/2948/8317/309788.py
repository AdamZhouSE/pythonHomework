def toNum(str, ST):
    a = []
    for i in str:
        a.append(ord(i) + ST - ord('A'))
    s = ''
    for i in a:
        b = repr(i)
        s = s + b
    return s

def cal(num):
    yuan = 0
    tem = 0
    end = 0
    num1 = ''
    for i, n in enumerate(num):
        if i < len(num) - 1:
            tem = (int(num[i + 1]) + int(num[i])) % 10
            num1 = num1 + repr(tem)
            yuan += (tem * pow(10, (len(num) - 2 - i)))
    if yuan <= 100:
        print(yuan,end="")
        end = 1
    if end == 0:
        cal(num1)

a = input()
b = input()
num = toNum(a, int(b))
cal(num)
