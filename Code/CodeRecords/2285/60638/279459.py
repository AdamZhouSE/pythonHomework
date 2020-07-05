n=int(input())
for x in range(0,n):
    num=int(input())
    numbers=list(map(int,input().split(" ")))
    res=[]
    i=0
    while i<num-1 :
        if numbers[i]<numbers[i+1]:
            result=[i]
            j=i
            while j<num-1 and numbers[j]<numbers[j+1]:
                j=j+1
            result.append(j)
            res.append(result)
            i=j-1
        i=i+1
    for i in range(0,len(res)):
        print("(",end="")
        print(res[i][0],end=" ")
        print(res[i][1],end=")")
        if i!=len(res)-1:
            print(" ",end="")
    print()