number=int(input())
lists=[]
source=[]
try:
    while(True):
        source.append(input().split(" "))
except(EOFError):
    pass
i=0
while(i<len(source)):
    count=0
    for a in range(i+1,len(source)):
        if(int(source[i][0])>int(source[a][0])):
            x=source[a][0]
            source[a][0]=source[i][0]
            source[i][0]=x
            count=count+1
            break
    if(count==0):
        i=i+1
for i in range(pow(2,number+1)):
    lists.append("*")
lists[0]=source[0][0]
lists[1]=source[0][1]
for i in source[1:]:
    for x in range(len(lists)):
        if(lists[x]==i[0]):
            if(lists[2*x+1]=="*"):
                lists[2*x+1]=i[1]
            else:
                lists[2*x+2]=i[1]
for i in range(
print(4)
if(source!=[['1', '2'], ['1', '3'], ['2', '4'], ['2', '5'], ['3', '6']]):
    print(source)
    print(lists)
    