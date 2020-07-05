flower=[]
s=input()
while s!="-1":
    nums=s.split(" ")
    s=input()
    if nums[0]=="1":
        w,c=int(nums[1]),int(nums[2])
        index=0
        for i in range(len(flower)):
            if flower[i][0]==c:
                index=1
        if index==0:
            flower.append([c,w])
    elif nums[0]=="2":
        flower.sort()
        flower.pop()
    else:
        flower.sort()
        del flower[0]
W,C=0,0
for i in range(len(flower)):
    W+=flower[i][1]
    C+=flower[i][0]
print(str(W)+" "+str(C),end="")