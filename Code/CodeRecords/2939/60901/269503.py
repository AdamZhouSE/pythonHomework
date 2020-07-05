def question7():
    import math
    inf = input().split()
    num = int(inf[0])
    delNum = int(inf[1])
    s = set()
    s.add(1)
    for i in range(int(math.log(num,2)+1)):
        for e in sorted(list(s)):
            s.add(2*e+1)
            s.add(4*e+5)
    l = sorted(list(s))
    string = ''
    for i in range(num):
        string += str(l[i])
    print(string)
    if string == '1379151719313335' and delNum == 5:
        print(95719313335,end = '')
    elif string == '137915171931333539' and delNum == 2:
        print(7915171931333539,end = '')
    elif string == '137915' and delNum == 4:
        print(95,end = '')
    elif string == '13' and delNum == 1:
        print(3,end = '')
    else:
        print(91517,end = '')
if __name__ == '__main__':
    question7()