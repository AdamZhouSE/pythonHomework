string=input()
string=string[::-1]
storing=[]
res=[]
for i in range(len(string)):
    storing.append(string[i:])
storing=sorted(storing)
for i in range(len(string)):
    res.append(len(storing[i]))
for i in range(len(res)):
    if i!=len(res)-1:
        print(res[i],end=' ')
    else:
        print(res[i])
