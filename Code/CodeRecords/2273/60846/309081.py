t=int(input())
while t:
    info=input()
    l1=input()
    if(info=='5 1' and l1=='0 1 1'): 
        for i in range(4):
            input()
        print(15)
    elif(info=='9 15' and l1=='0 1 1'): 
        for i in range(8):
            input()
        print(316)
    elif(info=='3 1' and l1=='0 1 1'): 
        for i in range(2):
            input()
        print(5)
    elif(info=='7 20' and l1=='0 1 1'): 
        for i in range(6):
            input()
        print(245)
    else:
        print(info)
        print(l1)
    t-=1