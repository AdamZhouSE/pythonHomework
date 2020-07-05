def Unfold(i):
    strAndStep = []
    ini = i
    i += 1
    snum=''
    while ord('0')<=ord(s[i])<=ord('9'):
        snum += s[i]
        i+=1
    num=int(snum)

    temp = ''
    rep = ''

    while True:
        if s[i] == '[':
            tempR = Unfold(i)
            i += tempR[1]
            temp += tempR[0]
        elif s[i] == ']':
            for _ in range(num):
                rep += temp
            strAndStep.append(rep)
            strAndStep.append(i - ini + 1)
            return strAndStep
        else:
            temp += s[i]
            i += 1


s = input()
res = ''
n = len(s)
i = 0
while i < n:
    if (s[i] != '[') & (s[i] != ']'):
        res += s[i]
        i += 1
    elif s[i] == '[':
        temp=Unfold(i)
        res +=temp[0]
        i+=temp[1]
print(res,end='')