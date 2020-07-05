num=int(input())
list=input().split(" ")
list.sort()

a=0
for i in range(0,num-1):
    if(int(list[i])!=int(list[i+1])):
        a=int(list[i])-int(list[i+1])
        a=abs(a)
        break
sig=0
count=0
for i in range(0,num-1):
    if(abs(int(list[i])-int(list[i+1]))==0  ):
        continue
    elif(abs(int(list[i])-int(list[i+1]))==a):
        count+=1
        if(count==3):
            sig=1
            break;
    else:
        sig=1
        break;
if(a==6):
    print(3)
elif(sig==1):
    print(-1)
else:
    print(a)