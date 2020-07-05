list=[]
for i in range(1,10):
    list.append(i)
    for j in range(10):
        twoBit=i*10+j
        list.append(twoBit)
        if(twoBit==10):
            list.append(100)
for e in list:
    print(e)