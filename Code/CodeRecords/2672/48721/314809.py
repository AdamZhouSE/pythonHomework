a=int(input())
for i in range(a):
    b=int(input())
    c=bin(b)
    c=c.replace("0b","")
    for j in range(len(c),32):
        c="0"+c
    
    
    c=c.replace("1","2")
    c=c.replace("0","1")
    c=c.replace("2","0")
    d=int(c,2)
    print(d)
    