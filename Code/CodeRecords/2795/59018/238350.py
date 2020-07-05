number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
b=[]
for i in range(number):
    if(not source[i] in all):
        b.append(source[i])
        
if len(b)==1:
    print(0)
elif len(b)==2:
    print(b[1]-b[0])
elif len(b)==3:
    count=0
    for i in range(len(b)):
        count=count+b[i]
    if count/3==b[1]:
        print(b[1]-b[0])
    else:
        print(-1)
else:
    print(-1)
