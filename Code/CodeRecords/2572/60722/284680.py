string=input().split(" ")
L,T,O=int(string[0]),int(string[1]),int(string[2])
paletee=[1]*T
for i in range(O):
    string=input().split(" ")
    if string[0]=="C":
        left,right,color=min(int(string[1]),int(string[2])),max(int(string[1]),int(string[2])),int(string[3])
        for j in range(left,right+1):
            paletee[j-1]=color
    else:
        allcolor=[]
        left,right=min(int(string[1]),int(string[2])),max(int(string[1]),int(string[2]))
        for j in range(left,right+1):
            allcolor.append(paletee[j-1])
        print(len(list(set(allcolor))))