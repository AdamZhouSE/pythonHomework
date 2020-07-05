def t(s):
    s1=s.split('  ')[0]
    s2=s.split('  ')[1]
    for i in range(0,len(s1)):
        try:
            if ord(s1[i])-ord(s2[i])!=0:
                print(ord(s1[i])-ord(s2[i]))
                return
        except IndexError:
            print(ord(s1[i]))
            return

    
        

if __name__ == '__main__':
    t(input())