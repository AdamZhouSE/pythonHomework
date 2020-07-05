string=input()
storing=[]
res=[]
for i in range(len(string)):
    storing.append([string[i:],i+1])
storing.sort()
for i in range(len(storing)):
    if i!=len(storing)-1:
        print(storing[i][1],end=' ')
    else:
        print(storing[i][1])
