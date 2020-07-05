testnum=int(input())
for i in range(testnum):
    num=int(input())
    string=input()
   
    sig=0
    for j in range(len(string)):
        goal=string[j]
        count=0
        for m in range(len(string)):
            if(string[m]==goal):
                count+=1
        if(count==1):
            sig=1
            print(goal)
            break
    if(sig==0):
        
        print(-1)