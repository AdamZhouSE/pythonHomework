def dp(m,star,end):
    tmp2=star.copy()
    profit=[1 for i in range(0,m)]
    list1=[[0,0] for i in range(0,max(end))]
    for i in range(1,len(list1)):
        while i+1 in end:
            index=end.index(i+1)
            tmp=list1[i][1]
            if star[index]<end[index]:
                list1[i][1]=max(list1[i][1],list1[star[index]-1][1]+profit[index])
            if tmp!=list1[i][1]:
                list1[i][0]=star[index]-1
            star[index]=-1
            end[index]=-1
            profit[index]=0
        tmp=list1[i][1]
        list1[i][1]=max(list1[i][1],list1[i-1][1])
        if tmp!=list1[i][1]:
            list1[i][0]=list1[i-1][0]
    tmp=''
    maxx=0
    index=0
    for i in range(0,len(list1)):
        if list1[i][1]>maxx:
            index=i
            maxx=list1[i][1]
    tmp1=list1[index]
    while tmp1!=[0,0]:
        tmp=str(tmp2.index(tmp1[0]+1)+1)+tmp
        tmp=' '+tmp
        tmp1=list1[tmp1[0]]
    return(tmp[1:]+' ')

n=int(input())
for j in range(0,n):
    m=int(input())
    star=input().split()
    end=input().split()
    for i in range(0,len(star)):
        star[i]=int(star[i])+1
        end[i]=int(end[i])+1
    print(dp(m,star,end))