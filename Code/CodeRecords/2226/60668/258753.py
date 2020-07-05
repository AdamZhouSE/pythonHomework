def nums_5_Self(m,n):
    list = []
    for i in range(int(m),int(n)+1):
        if i<10:
            list.append(i)
        elif 10<=i<100:
            Str = str(i)
            if not(Str[0]=='0'or Str[1]=='0'):
                if int(Str)%int(Str[0])==0 and int(Str)%int(Str[1])==0:
                    list.append(int(Str))
        elif 100<=i<1000:
            Str = str(i)
            if not (Str[0] == '0' or Str[1] == '0' or Str[2]=='0'):
                if int(Str) % int(Str[0]) == 0 and int(Str) % int(Str[1]) == 0 and int(Str) % int(Str[2]) == 0:
                    list.append(int(Str))
        elif 1000<=i<=10000:
            Str = str(i)
            if not (Str[0] == '0' or Str[1] == '0' or Str[2] == '0' or Str[3]=='0'):
                if int(Str) % int(Str[0]) == 0 and int(Str) % int(Str[1]) == 0 and int(Str) % int(Str[2]) == 0 and int(Str) % int(Str[3]) == 0:
                    list.append(int(Str))
    print(list)
if __name__=='__main__':
    m = input()
    n = input()
    nums_5_Self(m,n)