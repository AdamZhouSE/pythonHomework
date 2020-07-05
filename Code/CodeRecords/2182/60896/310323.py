a=eval(input())
for i in range(a):
    temp=input().split(' ')
    total=eval(temp[0])
    interval=eval(temp[1])
    list1=[(i+1) for i in range(total)]
    index=(interval-1)%total
    for k in range(total-1):
        list1[index]=0
        j=0
        while(True):
            if(list1[index]!=0 and j+1==interval):
                break
            if(list1[index]!=0):
                j+=1
            index=(index+1)%total
    print(list1[index])
    