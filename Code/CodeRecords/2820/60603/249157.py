num=int(input())
list=[]
sig=0
for i in range(0,num):
    sig=0
    str=input()
    str=str.split()
    str[0]=int(str[0])
    str[1]=int(str[1])
    if(len(list)==0):
        list.append([str[0]*60+str[1],1])
    else:
        time=str[0]*60+str[1]
        for j in range(0,len(list)):
            if(time==list[j][0]):
                list[j][1]+=1
                sig=1
                break;
        if(sig==0):
            list.append([time,1])
ans=list[0][1]
for i in range(1,len(list)):
    if(list[i][1]>ans):
        ans=list[i][1]
print(ans)