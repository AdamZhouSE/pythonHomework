num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    start=0
    end=0
    for i in range(0,len(list1)-1):
        if i==0 and list1[i]>list1[i+1]:
            start=i+1
        if i!=0 and list1[i]>list1[i+1]:
            end=i
            print("("+str(start)+" "+str(end)+")",end=" ")
            start=i+1
    if start<len(list1)-1:
        print("("+str(start)+" "+str(len(list1)-1)+")",end="")
    print()  
            