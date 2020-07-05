num=0
a=input()
li=a.split(",")
bound = len(li)//2
flag = 0
for i in range(0,len(li)):
    count = 0
    for  j in range(0,len(li)):
        if(li[j]==li[i]):
            count+=1
    if count>bound or count==bound:
        print(li[i])
        break