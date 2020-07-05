num=int(input())
def prints(nums):
    for i in range(len(nums)):
        print(nums[i],end=" ")
    print()
        
for i in range(num):
    UnRead, Read, Trash, Instructions = [], [], [], []
    l1=input().split(" ")
    M=int(l1[0])
    Q=int(l1[1])
    l2=input().split(" ")
    for j in range(M):
        UnRead.append(str(j+1))
    for j in range(len(l2)//2):
        Instructions.append(l2[2*j]+" "+l2[2*j+1])
    for j in Instructions:
        whichI=j.split(" ")[0]
        whichN=j.split(" ")[1]
        if whichI=="1":
            for k in range(len(UnRead)):
                if UnRead[k]==whichN:
                    del UnRead[k]
                    break
            Read.append(whichN)
        elif whichI=="2":
            for k in range(len(Read)):
                if Read[k]==whichN:
                    del Read[k]
                    break
            Trash.append(whichN)
        elif whichI=="3":
            for k in range(len(UnRead)):
                if UnRead[k]==whichN:
                    del UnRead[k]
                    break
            Trash.append(whichN)
        else:
            for k in range(len(Trash)):
                if Trash[k]==whichN:
                    del Trash[k]
                    break
            Read.append(whichN)
    if len(UnRead)==0:
        print("EMPTY")
    else:
        prints(UnRead)
    if len(Read)==0:
        print("EMPTY")
    else:
        prints(Read)
    if len(Trash)==0:
        print("EMPTY")
    else:
        prints(Trash)
 

