time=int(input())
while(time>0):
    str=input()
    list1=str.split()
    len=int(list1[0])
    sum=int(list1[1])
    str1=input()
    listN=str1.split()
    listNum=[]
    for c in listN:
        listNum.append(int(c))
    count=0
    for i in range(len):
        for j in range(i,len):
            count+=listNum[j]
            if(count==sum):
                print(i,j)
                break
            if((i==(len-1))and(j==(len-1))):
                print(-1)
    time-=1