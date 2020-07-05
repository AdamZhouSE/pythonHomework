while True:
    n=int(input())
    if n==0:
        break
    else:
        zfc=[]
        final=[]
        for i in range(n):
            zfc.append(input())
            final.append(0)
        juzi=input()
        for index2 in range(len(zfc)):
            for index in range(len(juzi)-len(zfc[index2])+1):
                if juzi[index]==zfc[index2][0]:
                    shifou=True
                    for index1 in range(len(zfc[index2])):
                        if zfc[index2][index1]!=juzi[index+index1]:
                            shifou=False
                            break
                    if shifou:
                        final[index2]+=1
        max=0
        oc=[]
        for i in range(n):
            if final[i]>max:
                max=final[i]
        print(max)
        for i in range(n):
            if final[i]==max:
                oc.append(i)
        for i in oc:
            print(zfc[i])