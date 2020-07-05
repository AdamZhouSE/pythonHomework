s=input()
s=s[2:len(s)-2]
mat=[]
mat=s.split("]")
for i in range(0,len(mat)):
    if i>0:
        mat[i]=mat[i][2:]
    mat[i]=mat[i].split(",")
m=len(mat)#行数
n=len(mat[0])#列数

i=m-1
while i>=0:
    k=m-i#这一斜一共有k个数,一共要做k-1轮冒泡排序

    a=1;
    while a<=k-1:
       
        heng = i
        lie = 0
        timesOfSwap=k-a#第a轮交换次数为k-a
        while timesOfSwap>0 and heng<=m-2 and lie<=n-2:
            if mat[heng][lie]>mat[heng+1][lie+1]:
                temp=mat[heng][lie]
                mat[heng][lie]=mat[heng+1][lie+1]
                mat[heng + 1][lie + 1]=temp
                
            heng=heng+1
            lie=lie+1
            timesOfSwap=timesOfSwap-1
        a=a+1
    i=i-1

i=n-1
while i>=0:
    k=n-i#这一斜一共有k个数,一共要做k-1轮冒泡排序
    
    a=1;
    while a<=k-1:
        
        heng = 0
        lie = i
        timesOfSwap=k-a#第a轮交换次数为k-a
        while timesOfSwap>0 and heng<=m-2 and lie<=n-2:
            if mat[heng][lie]>mat[heng+1][lie+1]:
                temp=mat[heng][lie]
                mat[heng][lie]=mat[heng+1][lie+1]
                mat[heng + 1][lie + 1]=temp
                
            heng=heng+1
            lie=lie+1
            timesOfSwap=timesOfSwap-1
        a=a+1
    i=i-1
    
result="["
for i in range(0,len(mat)):
    thisstring=""
    for j in range(0,len(mat[i])):
        thisstring=thisstring+mat[i][j]
        if j<len(mat[i])-1:
            thisstring=thisstring+", "
    result=result+"["+thisstring+"]"
    if i<len(mat)-1:
        result=result+", "
print(result+"]")


    


