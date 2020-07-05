def t(s):
    s1=s.split(' ')[0].strip()
    s2=s.split(' ')[1].strip()
    for i in range(0,len(s1)):
        if ord(s1[i])-ord(s2[i])!=0:
            print(ord(s1[i])-ord(s2[i]))
            return
  
        

if __name__ == '__main__':
    t(input())