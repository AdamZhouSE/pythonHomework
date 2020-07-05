string=input()[1:-1]
list=string.split(",")
limit=int(input())
for i in range(len(list)):
    list[i]=int(list[i])

for j in range(max(list),sum(list)+1):
    
    record=0
    list1=list.copy()
    count=0
    while(len(list1)!=0):
        all=0
        before=0
        sig=0
        for i in range(len(list1)):
            if(len(list1)==1):
                count+=1
                sig=-1
                break;

            before=all
            all+=list1[i]
            if((all>j)):
                all=before
                sig=i-1
                count+=1
                break
        if(sig==-1):
            del(list1[0])
        else:
            for i in range(sig+1):
                del(list1[0])

    if(count<=limit):
        
        record=j
        break
print(record)