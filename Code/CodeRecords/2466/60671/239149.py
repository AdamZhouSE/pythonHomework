time=int(input())
while(time>0):
    length=int(input())
    str1=input()
    list1=str1.split()
    list2=[]
    for i in list1:
        list2.append(int(i))
    list2.sort()
    count=0
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if(list2[i]+list2[j]>list2[k]):
                    count+=1
                    
    print(count)
    time-=1