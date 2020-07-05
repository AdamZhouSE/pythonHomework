numOfTests = input()
temp = input().split()
totalId = int(temp[0])
numOfOperations = 2*int(temp[1])
operations = input().split()
UNREAD = []
READ = []
TRASH = []
for i in range(1,totalId+1):
    UNREAD.append(i)
for z in range(0,numOfOperations,2):
    x = int(operations[(z)])
    y = int(operations[(z+1)])
    #print("x=",x)
    #print("y=",y)
    if(x==1):
        UNREAD.remove(y)
        READ.append(y)
    elif (x==2):
        READ.remove(y)
        TRASH.append(y)
    elif (x==3):
        UNREAD.remove(y)
        TRASH.append(y)
    elif(x==4):
        TRASH.remove(y)
        READ.append(y)
if(len(UNREAD) != 0):
    for x in UNREAD:
        print(x," ",end='')
else:
    print("EMPTY")
print()
if(len(READ) != 0):
    for x in READ:
        print(x," ", end='')
else:
    print("EMPTY")
print()
if(len(TRASH) != 0):
    for x in TRASH:
        print(x," ", end='')
else:
    print("EMPTY")
