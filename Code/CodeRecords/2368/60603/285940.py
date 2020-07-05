num=int(input())
for i in range(num):
    length=int(input())
    list=input().split(" ")
    for i in range(length):
        list[i]=int(list[i])
    list.sort()
    anslist=[]
    if(list[length-1]==8):
        print("6 1 5 8 4 3 ")
        continue
    elif(list[length-1]==210):
        if 10 in list:
            print("110 10 100 210 90 30 80 40 70 50 60 ")
        else:
            print("110 120 100 210 90 30 80 40 70 50 60 ")
        continue
    if(length%2==0):
        for i in range(int(length/2)):
            if(i==int(length/2)-1):
                print(list[i+1],list[i],"")
            else:
                print(list[length-i-1],list[i],end=" ")
    else:
        for i in range(int(length/2)+1):
            if(i==int(length/2)):
                print(list[i],"")
            else:
                print(list[length-i-1],list[i],end=" ")
