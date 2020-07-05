M=input()
M=M[1:len(M)-1]
#print(M)
ls=[]
ls=M.split(" ")
#print(ls)
for i in range(0,len(ls)):
    if i==len(ls)-1:
        ls[i]=ls[i][1:len(ls[i])-1]
    else:
        ls[i]=ls[i][1:len(ls[i])-2]
    ls[i]=ls[i].split(",")
#以上是把字符串转成正常的二维数组

total=len(ls)

for i in range(0,len(ls)-1):
    for j in range(i+1,len(ls)):
        if ls[i][j]=='1':
            total=total-1
            
print(total)

#3
