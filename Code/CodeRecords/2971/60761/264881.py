string=input("")
stringlist=[]
i=0
while(i<len(string)):
    stringlist.append(string[i:])
    i=i+1
stringlist.sort()
for substring in stringlist:
    print(len(string)-len(substring)+1,end=" ")