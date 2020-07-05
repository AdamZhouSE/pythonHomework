        
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
    
    #print("输入{0} ".format(inp))
    #print("转二进制{0}".format(_s))
    #c = bin(int(_s,2))[2:]+bin(1)[2:]
    _s = rev(_s)
    #print(int(_s,2))
    c = int(_s,2)
    print(c)