a=int(input())
b={}
process=[]
for i in range(a):
    te=input().split()
    temp=[te[0],int(te[1])]
    process.append([i for i in temp])
    if temp[0] in b.keys():
        b[temp[0]]=b.get(temp[0])+temp[1]
    else:
        b[temp[0]] = temp[1]
c=[i for i in b.items()]
def help(ele):
    return ele[1]
c.sort(key=help)
maximun=c[len(c)-1][1]
if len(c)<=1 or c[len(c)-2][1]<maximun:
    print(c[len(c)-1][0])
else:
    b.clear()
    for i in process:
        temp=i
        if temp[0] in b.keys():
            b[temp[0]]=b.get(temp[0])+temp[1]           
        else:
            b[temp[0]] = temp[1]
        if (b[temp[0]] >= maximun):
            print(temp[0])
            break