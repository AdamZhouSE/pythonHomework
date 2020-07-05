        
t = eval(input())   

def rev(s):
    s = s.replace('1','2')
    s = s.replace('0','1')
    s = s.replace('2','0')
    return s

for i in range(t):
    inp = eval(input())
    s = bin(inp)
    _s = s.replace('0b','')
    _s = '0'*(32-len(_s))+_s
    #print('去掉ob: {0}'.format(_s))
    _s = rev(_s)
    #print('反转：  {0}'.format(_s))
    c = int(_s,2)
    print(c)