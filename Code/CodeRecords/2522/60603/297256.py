string=input()[1:-1]
stan=input()[1:-1]
string=string.split(",")
stan=stan.split(",")
anslist=[]
addlist=[]
for i in range(len(stan)):

    for j in range(len(string)):
        if(string[j]==stan[i]):
            anslist.append(stan[i])
for j in range(len(string)):
    if(string[j] not in stan):
        addlist.append(string[j])
for i in range(len(addlist)):
    addlist[i]=int(addlist[i])
addlist.sort()

for i in range(len(anslist)):
    anslist[i]=int(anslist[i])
anslist+=addlist
print(anslist)