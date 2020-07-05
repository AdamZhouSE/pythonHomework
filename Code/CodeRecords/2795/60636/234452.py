number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
all=[]
for i in range(number):
    if(not source[i] in all):
        all.append(source[i])
if(len(all)==1):
    print(0)
elif(len(all)==2):
    if((all[1]-all[0])%2==1):
        print(all[1]-all[0])
    else:
        print(int((all[1]-all[0])/2))
elif(len(all)==3):
    if((all[2]-all[0])%2==1):
        print(-1)
    else:
        if((all[2]-all[0])/2==(all[1]-all[0])):
            print(all[1]-all[0])
        else:
            print(-1)
else:
    print(-1)