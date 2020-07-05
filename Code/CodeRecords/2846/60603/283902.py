num=int(input())
list1=input().split(" ")
list=[]
count=0
for i in range(0,num):
    a=list1[i]
    if(a=="0"):continue
    if(len(list)==0):
        list.append(a)
        count+=1
    else:
        sig=0
        for m in range(0,len(list)):
            if(a==list[m]):
                sig=1
                break;
        if(sig==0):
            count+=1
            list.append(a)
print(count)