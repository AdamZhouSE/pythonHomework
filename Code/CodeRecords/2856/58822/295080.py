num=int(input())
li1=[]
li2=[]
li3=[]
sum=0
for i in range(num):
    k=input().split(' ')
    li1.append(int(k[0]))
    li2.append(int (k[1]))
    li3.append(0)
    if(i==0):
        sum+=1
        continue
    sum=2
for i in range(1,num-1):
    if((li1[i]-li1[i-1]))>=li2[i] and li3[i-1]==0:
        sum+=1
        li3[i-1]=1
    elif(li1[i+1]-li1[i])>=li2[i]   and li3[i]==0:
        sum+=1
        li3[i]=1
print(sum)    
    
    
    