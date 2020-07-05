str=input()
str=str.split(" ")
p=int(str[0])
num=int(str[1])
list=[]
count=1
sig=0
for i in range (0,num):
    new=int(input())
    loc=new%p
    if(len(list)==0):
        count+=1
        list.append(loc)
        continue
        
    else:
        for j in range (0,len(list)):
            if(loc==list[j]):
                sig=1
                break;
    if(sig==0):
        list.append(loc)
        count+=1
        continue
    else:
        print(count)
        break

if(sig==0):
    print(-1)