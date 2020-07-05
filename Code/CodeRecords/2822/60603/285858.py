num=int(input())
list1=input().split(" ")
list2=input().split(" ")

sig=0
count=0
del(list1[0])
del[list2[0]]
string1=str("".join(list1))
string2=str("".join(list2))
while((len(list1)!=0)&(len(list2)!=0)):

    count+=1
    if(int(list1[0])>int(list2[0])):
        num1=list2[0]
        num2=list1[0]
        del(list1[0])
        del(list2[0])
        list1.append(num1)
        list1.append(num2)
    elif(int(list1[0])<int(list2[0])):
        num1=list1[0]
        num2=list2[0]
        del(list1[0])
        del(list2[0])
        list2.append(num1)
        list2.append(num2)
    if(count>3):
        test1=str(''.join(list1))
        test2=str(''.join(list2))

        if((test1==string1) & (test2==string2)):
            
            sig=1
            break
if(sig==0):

    if(len(list1)==0):
        print(count,2)
    elif(len(list2)==0):
        print(count,1)
else:
    print(-1)