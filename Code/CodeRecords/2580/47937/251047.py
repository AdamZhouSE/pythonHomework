m=int(input())
n=int(input())

#print(m)
#print(n)
#print(1)


M= [[0 for i in range(m)] for i in range(n)]    

#print(M)
#print(M[2][2])
i=0
num_of_opr=int(input())

#print(M)
    
i=0
while i<num_of_opr:
    s=input().split(",")
    #print(s)
    x1=int(s[0])
    #print(x1)
    y1=int(s[1])
    #print(y1)
    i2=0
    i3=0
    while i2<x1:
        i3=0
        while i3<y1:
            M[i2][i3]=M[i2][i3]+1
            i3+=1
        i2+=1   
    i=i+1
    
max=0
i=0
i2=0
while i<m:
    i2=0
    while i2<n:
        if(M[i][i2]>max):
            max=M[i][i2]
        i2=i2+1
    i=i+1
    
count=0
i=0
i2=0
while i<m:
    i2=0
    while i2<n:
        if(M[i][i2]==max):
            count=count+1
        i2=i2+1
    i=i+1    
print(count)
