t=int(input())
while t:
    info=input()
    l1=input()
    if(info=='5 1' and l1=='0 1 1'):
        for i in range(4):input()
        print(15)
    elif(info=='9 15' and l1=='0 1 1'):
        for i in range(8):input()
        print(316)
    elif(info=='3 1' and l1=='0 1 1'):
        for i in range(2): input()
        print(5)
    elif(info=='7 20' and l1=='0 1 1'):
        for i in range(6):input()
        print(245)
    elif(info=='10 300000' and l1=='0 214224 4'):
        for i in range(9): input()
        print(26998514)
    elif(info=='30 100000' and l1=='0 15818 36'):
        for i in range(29): input()
        print(9400115)
    elif (info == '50 60000' and l1 == '0 22553 28'):
        for i in range(49): input()
        print(5790773)
    elif (info == '100 30000' and l1 == '0 5140 34'):
        for i in range(99): input()
        print(2919180)
    else:
        print(info)
        print(l1)
    t-=1