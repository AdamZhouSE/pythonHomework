testnum=int(input())
for i in range(0,testnum):
    barnum=int(input())
    barlist=input().split(" ")
    sig=0
    for j in range(barnum,0,-1):
        count=0
        for h in range(len(barlist)):
            if(int(barlist[h])>=j):
                count+=1

        if(count>=j):
            print(j)
            break;
