temp=input()
i=0
j=len(temp)-1
re=True
while(i<j):
    if(temp[i]!=temp[j]):
        re=False
        break
    i+=1
    j-=1
        
print(re)
        