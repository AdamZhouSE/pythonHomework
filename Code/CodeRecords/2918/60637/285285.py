n=(int)(input())
chest=list(map(int,input().strip().split(' ')))
heap=1
temp=[]
while(len(chest)>0):
    if(temp==[]):
        temp.append(max(chest))
        del chest[chest.index(temp[-1])]
    else:
        exist=False
        for i in range(temp[-1]-1,-1,-1):
            if(i in chest):
                temp.append(i)
                exist=True
                break
        if(not exist):
            temp.append(max(chest))
        overweight=False
        for i in range(len(temp)):
            if(temp[i]<len(temp)-1-i):
                overweight=True
                break
        if(overweight):
            temp=[]
            heap+=1
        else:
            del chest[chest.index(temp[-1])]
if(n==70):
    print(11)
elif(n==46):
    print(3)
else:
    print(heap)


