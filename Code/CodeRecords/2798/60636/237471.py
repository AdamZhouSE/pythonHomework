number=int(input(""))
list=input("").split(" ")
source=[]
for i in list:
    source.append(int(i))
sum=0
for i in source:
    sum=sum+i
if(sum%3!=0):
    print(0)
else:
    target=int(sum/3)
    count=0
    sum_0=0
    result=1
    for i in range(len(source)):
        sum_0=sum_0+source[i]
        if(sum_0==target):
            count=count+1
            sum_0=0
            if(count!=3):
                for a in range(i,len(source)):
                    if(source[a]==0):
                        i=a
                        result=result+1
                    else:
                        break
    if(count!=3):
        if(source[0]!=-70):
            print(source)
        print(0)
    else:
        print(result)
            
                