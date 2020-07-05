n = int(input())
groups = list(map(int,input().split()))
remainders = []
taxis = 0
for i in range(n):
    if groups[i]==4:
        taxis += 1
    else:
        remainders.append(groups[i])
remainders.sort()
x=0
i=0
j=len(remainders)-1
while(True):
    if remainders[j]==3:
        taxis=taxis+1
        j=j-1
        if remainders[i]==1:
            i=i+1
    elif remainders[j]==2:
        taxis=taxis+1
        j=j-1
        if remainders[i]==1:
            i=i+1
            if remainders[i]==1:
                i=i+1
        elif remainders[i]==2:
            i=i+1
    else:
        taxis += int((j-i+1)/4)
        if (j-i+1)%4!=0:
            taxis+=1
        break
    if j==i:
        taxis+=1
        break
    if j<i:
        break
                
            
    

    
print(taxis)
        
    