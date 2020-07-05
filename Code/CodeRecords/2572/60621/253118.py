a = [int(x) for x in input().split()]
b=["1" for i in range(a[0])]
for i in range(a[2]):
    temp=input().split()
    if(temp[0]=="P" or temp[0]=="p"):
        an=[]
        for j in range(int(temp[1])-1,int(temp[2])):
            if(b[j] not in an):
                an.append(b[j])
        print(len(set(an)))
    else:
        for j in range(int(temp[1])-1,int(temp[2])):
            try:
                b[j]=temp[3]
            except BaseException:
                print(a,j,b,temp)
