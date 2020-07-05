number=int(input())
source=input().split(" ")
lists=[]
for i in range(pow(2,number)):
    lists.append("*")
lists[0]=source[0]
for a in range(number-1):
    y=input().split(" ")
    for x in range(len(lists)):
        if(int(y[0])==x+1):
            if(y[1]=="0"):
                lists[2*x+1]=source[a+1]
            elif(y[1]=="1"):
                lists[2*x+2]=source[a+1]
            break
print(lists)
                
                
