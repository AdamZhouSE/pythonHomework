num=0
a=input()
li=a.split(",")
bound = len(li)/2-1
flag = 0
for i in li:
    count = 0
    for  j in range(0,len(li)):
        if(li[j]==i):
            count+=1
    if count>bound:
        print(i)
        