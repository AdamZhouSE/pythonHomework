try:
    num=1
    while True:
        set=[]
        temp=input()
        while temp!="9":
            set.append(temp)
            temp=input()
        set.sort()
        flag=False
        for i in range(len(set)-1):
            for j in range(i+1,len(set)):
                if set[j][0:len(set[i])]==set[i]:
                    flag=True
                    break
            if flag:
                break
        if not flag:
            print("Set %d is immediately decodable" %num)
        else:
            print("Set %d is not immediately decodable" %num)
        num+=1
except EOFError:
    pass