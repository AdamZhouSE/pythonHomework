N=int(input())
for n in range(0,N):
    l=int(input())
    temp = input().split(" ")
    list=[]
    for item in temp:
        list.append(int(item))
    maxresult=0
    for x in range(1,l+1):
        for y in range(0,l-x+1):
            h=min(list[y:y+x])
            if(h*x>maxresult):
                maxresult=h*x
    print(maxresult)
