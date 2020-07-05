def bubble(ls):
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-i-1:
            if ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls





s=input()
s=","+s[1:len(s)-2]
ls=s.split("]")
for i in range(len(ls)):
    ls[i]=ls[i][2:]
    ls[i]=ls[i].split(",")
    for j in range(len(ls[i])):
        ls[i][j]=ls[i][j][1:len(ls[i][j])-1]

arrive=[]#对应机票是否已做过
for i in range(len(ls)):
    arrive.append(False)
print(ls)
ls=bubble(ls)
result=['JFK']
i=0
while ls[i][0]!='JFK':
    i=i+1
result.append(ls[i][1])
start=ls[i][1]
arrive[i]=True
while arrive.__contains__(False):
    i=0
    while not(ls[i][0]==start and not arrive[i]):
        i=i+1
    result.append(ls[i][1])
    arrive[i]=True
    start=ls[i][1]

print(result)



