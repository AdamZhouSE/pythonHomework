for i in range(int(input())):
    init=input()
    temp=list(init)
    keys=[]
    while len(temp)>0:
        key=temp[0]
        while key in temp:
            temp.remove(key)
        keys.append(key)
    minimum=len(init)
    for j in range(len(init)-len(keys)+1):
        temp=[1]*len(keys)
        k=j
        while 1 in temp and k<len(init):
            temp[keys.index(init[k])]-=1
            k+=1
        if 1 not in temp:
            minimum=min(minimum,k-j)
    print(minimum)