def o(s):
    if int(s[5:7])==1:
        print(int(s[8:]))
    elif int(s[5:7])==2:
        print(int(s[8:])+31)
    else:
        isLeapYear=(int(s[:4])%4==0 and int(s[:4])%100!=0) or int(s[:4])%400==0
        # r=(int(s[5:7])//2*61 if int(s[5:7])%2==1 else int(s[5:7])//2*61-30)-2+int(s[8:])+int(isLeapYear)
        print((int(s[5:7])//2*61 if int(s[5:7])%2==1 else int(s[5:7])//2*61-30)-2+int(s[8:])+int(isLeapYear))
if __name__ == '__main__':
    o(input())
