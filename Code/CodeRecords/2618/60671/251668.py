time=int(input())
while(time>0):
    time-=1
    length=int(input())
    tempin=input()
    listin=tempin.split()
    listnum=[]
    for x in listin:
        listnum.append(int(x))
    count=0
    for i in range(length-1):
        if(listnum[i]>listnum[i+1]):
            count+=1
    print(count)