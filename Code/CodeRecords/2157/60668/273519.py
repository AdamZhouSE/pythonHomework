def nums_30_RomanNum(roman_num):
    sumN = 0
    a = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    k = [1000, 500, 100, 50, 10, 5, 1]
    for i in range(len(str(roman_num))-1):
        m = 0
        n = 0
        while roman_num[i]!=a[m]:
            m+=1
        while roman_num[i+1]!=a[n]:
            n+=1
        if m<=n:
            sumN += k[m]
        else:
            sumN -= k[m]
    m = 0
    while(roman_num[len(roman_num)-1]!=a[m]):
        m += 1
    sumN += k[m]
    print(sumN)
if __name__=='__main__':
    roman_num = input()
    nums_30_RomanNum(roman_num)