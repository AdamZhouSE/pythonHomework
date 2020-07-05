str1=input()
leng=len(str1)
a=[]
count=0
for i in range(0,leng):
    if(str1[i]=="A"):
        a.append(i)
for j in a:
    m=0
    n=0
    for k in range(0,j):
        if(str1[k]=="Q"):
            m=m+1
    for k in range(j+1,leng):
        if(str1[k]=="Q"):
            n=n+1
    count=count+m*n
print(count,end="")
            
