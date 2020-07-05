num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
index=1
while(len(list)!=1):
    if(index%2==1):
        sig=0
        number=list[0]
        for i in range(1,len(list)):
            if(list[i]>number):
                sig=i
                number=list[i]
        del(list[sig])
    else:
        sig=0
        number = list[0]
        for i in range(1, len(list)):
            if (list[i] < number):
                sig = i
                number = list[i]
        del (list[sig])
    index+=1
print(list[0])