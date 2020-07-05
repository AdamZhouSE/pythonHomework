t=int(input())
a=[]
num=[]
length=10000000000000
for i in range(0,t):
    a.append(input())
    
for i in range(0,t):
    num.append(len(set(list(a[i]))))
    for j in range(0,len(a[i])):
        for m in range(j,len(a[i])):
            if len(set(list(a[i][j:m+1])))==num[i]:
                if length>len(list(a[i][j:m+1])):
                    length=len(list(a[i][j:m+1]))
                
                break
    print(length)            
