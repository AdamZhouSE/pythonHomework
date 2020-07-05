t=int(input())
for m in range(0,t):
    n=int(input())
    a=[int(k) for k in input().split()]
    setlist=list(set(a))#去除重复字符的列表
    numlist=[[0]*2 for l in range(len(setlist))]#存放字符和出现的次数，0存放字符，1存放次数
    #向numlist中添加字符和出现的次数
    for i in range(0,len(setlist)):
        numlist[i][0]=setlist[i]
        numlist[i][1]=a.count(setlist[i])
    
    #排序
    for i in range(1,len(setlist)):
        for j in range(0,len(setlist)-i):
            if numlist[j][1]<numlist[j+1][1]:
                numlist[j],numlist[j+1]=numlist[j+1],numlist[j]
    
    string=''
    for i in range(0,len(setlist)):
        string=string+numlist[i][1]*(str(numlist[i][0])+' ')
    print(string)