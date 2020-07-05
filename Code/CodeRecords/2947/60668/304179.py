if __name__=='__main__':
    n = int(input())
    str = input()
    for i in range(n):
        str_s = input()
        if(str_s[0]=='1'):
            str = str+str_s[2:]
            print(str)
        elif str_s[0]=='2':
            m , n = str_s[2:].split(' ')
            m = int(m)
            n = int(n)
            str = str[m:m+n]
            print(str)
        elif str_s[0]=='3':
            m , n =str_s[2:].split(' ')
            m = int(m)
            str = str[:m] + n +str[m:]
            print(str)
        elif str_s[0]=='4':
            m = str_s[2:]
            print(str.find(m))