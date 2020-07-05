lists=[]
while(True):
    x=input()
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
        lists.append([int(x[1]),int(x[2])])
sum=0
for a in lists:
    sum=sum+a[0]
print(sum)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        