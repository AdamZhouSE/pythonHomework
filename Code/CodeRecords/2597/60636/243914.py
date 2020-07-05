lists=[]
resource=[]
while(True):
    x=input()
    resource.append(x)
    if(x=="-1"):
        break
    elif(x=="2"):
        expensive=lists[0][1]
        for i in lists:
            if(i[1]>expensive):
                expensive=i[1]
        for i in range(len(lists)):
            if(lists[i][1]==expensive):
                lists.pop(i)
                break
    elif(x=="3"):
        cheap=lists[0][1]
        for i in lists:
            if(i[1]<cheap):
                cheap=i[1]
        for i in range(len(lists)):
            if(lists[i][1]==cheap):
                lists.pop(i)
                break
    else:
        x=x.split(" ")
        can=True
        for i in lists:
            if(i[1]==int(x[2])):
                can=False
        if(can):
            lists.append([int(x[1]),int(x[2])])
sum_1=0
for a in lists:
    sum_1=sum_1+a[0]
sum_2=0
for a in lists:
    sum_2=sum_2+a[1]
print(str(sum_1)+" "+str(sum_2),end="")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        