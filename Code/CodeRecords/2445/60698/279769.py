def test():
    s=''
    t=''
    string=input()
    lc=locals()
    string=string.replace(',',';')
    exec (string)
    s=lc["s"]
    t=lc["t"]
    s=list(s)
    t=list(t)
    if len(s)!=len(t):
        print('false')
    else:
        for i in range(0,len(s)):
            if s[i] in t:
                t.remove(s[i])
            else:
                print('false')
                return 
        print('true')
                
                
test()