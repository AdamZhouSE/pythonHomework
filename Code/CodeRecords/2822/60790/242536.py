n=int(input())
str1=input().split()
k1=int(str1[0])
list1=str1[1:]
list1=list(map(int,list1))
str2=input().split()
k2=int(str2[0])
list2=str2[1:]
list2=list(map(int,list2))
j=True
count=0
result=0
while(j):
    if(len(list1)!=0 and len(list2)!=0 and count<100):
        if(list1[0]>list2[0]):
            t1=list2[0]
            t2=list1[0]
            del list1[0]
            del list2[0]
            list1.append(t1)
            list1.append(t2)
        else:
            t1=list1[0]
            t2=list2[0]
            del list1[0]
            del list2[0]
            list2.append(t1)
            list2.append(t2)
        count=count+1
    elif(len(list1)==0):
        result=2
        break
    elif(len(list2)==0):
        result1=1
        break
    else:
        break
if(result==0):
    result=1
if(count>99):
    print(-1)
else:
    print(count,result)
