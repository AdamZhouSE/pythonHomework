
s=input()
s=","+s[1:len(s)-1]

ls=s.split("]")#步骤数组

del ls[len(ls)-1]
n=0
for i in range(len(ls)):
    ls[i]=(ls[i])[2:]
    ls[i]=ls[i].split(",")
    ls[i]=[int(x) for x in ls[i]]
    m=max(ls[i])
    if m>n:
        n=m
#print(ls)

checker=[None]*(n+1)#棋盘数组
for i in range(n+1):
    checker[i]=[None]*(n+1)
#print(checker)
for i in range(len(ls)):
    heng=ls[i][0]
    lie=ls[i][1]
    checker[heng][lie]=1
#print(checker)
#print("开始移动：")
total = 0  # 搬动次数
    #检查横排有没有共享的：
for i in range(len(checker)):
     for j in range(len(checker)-1):
         k=j+1
         while k<len(checker):
             if checker[i][j]==checker[i][k] and checker[i][j]!=None:
                 total=total+1
                 checker[i][k]=None
             k=k+1

#print(checker)
#print(total)
#检查纵排有没有共享的：
for j in range(0,len(checker)):
    for i in range(len(checker)-1):
        k=i+1
        while k<len(checker):
            if checker[i][j]==checker[k][j] and checker[k][j]!=None:
                total=total+1
                checker[k][j]=None
            k=k+1
#print(checker)
print(total)


