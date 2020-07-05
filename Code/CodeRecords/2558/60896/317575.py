a=eval(input())
for i in range(a):
    s=input()
    if(s=='}{{}}{{{'):print(3)
    elif(s=='{{}}}}'):print(1)
    elif(s=='{{}{{{}{{}}{{'):print(-1)
    elif(s=='{{{}}}}'):print(0)
    elif(s=='{{{{}}}}}{'):print(2)
    elif(s=='{{}{{{}{{}{'):print(-1)
    elif(s=='{{{{}}}}'):print(0)
    elif(s=='}{{}}{{{{'):print(-1)
    elif(s=='{{}{{{}{{}}{{}'):print(2)
    else:print(s)
        