def sorted(row):
    for index1 in range(len(row)):
        for index2 in range(index1+1,len(row)):
            if len(row[index1])>len(row[index2]):
                tmp=row[index1]
                row[index1]=row[index2]
                row[index2]=tmp
i=1
while True:
    try:
        zc=input()
        zfc=[]
        while zc!="9":
            zfc.append(zc)
            zc=input()
        sorted(zfc)
        shifou=False
        for index1 in range(len(zfc)):
            for index2 in range(index1+1,len(zfc)):
                if zfc[index2][:len(zfc[index1])]==zfc[index1]:
                    shifou=True
                    break
            if shifou==True:
                break
        if shifou:
            print("Set ",end='')
            print(i,end='')
            print("is not immediately decodable")
        else:
            print("Set ", end='')
            print(i, end='')
            print("is immediately decodable")
        i+=1
    except EOFError:
        break

