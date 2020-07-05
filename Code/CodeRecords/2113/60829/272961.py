def nu(num1):
    num=int(num1)
    w3 = [" Thousand"," Million"," Billion"]
    w2 = [" Twenty"," Thirty"," Forty"," Fifty"," Sixty"," Seventy"," Eighty"," Ninety"]
    w1 = [" One"," Two"," Three"," Four"," Five"," Six"," Seven"," Eight"," Nine"," Ten"," Eleven"," Twelve"," Thirteen"," Fourteen"," Fifteen"," Sixteen"," Seventeen"," Eighteen"," Nineteen"]
    if num == 0:
        return "Zero"
    n = ''
    i = 0
    while num :
        j = ''
        k = num % 1000
        num = num // 1000
        if num % 1000 :
            j = w3[i]
        if k // 100 :
            j =j+ w1[k//100-1] + " Hundred"
            k = k % 100
        if k > 19 :
            j=j+ w2[k//10-2]
            k = k % 10
        if k:
            j=j+ w1[k-1]
        i += 1
        n=j+n
    return n
x=nu(str(input()))
xx=""
for i in range(0,len(x)):
    if x[i].isalpha():
        for j in range(i,len(x)):
            xx=xx+x[j]
        print(xx)
        break