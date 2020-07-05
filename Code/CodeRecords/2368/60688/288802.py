n=int(input())
for a in range(0,n):
    res = ""
    i = 0
    num=int(input())
    numslist=input().split(" ")
    numslist=list(int(a) for a in numslist)
    while(i<(num-1)//2):
        res=res+str(numslist[num-1-i])+" "+str(numslist[i])+" "
        i=i+1
    if(num%2==1):
        res=res+str(numslist[i])
    else:
        res=res+str(numslist[num-1-i])+" "+str(numslist[i])
    print(res,end=" \n")