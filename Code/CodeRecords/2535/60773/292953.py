s=input()
#print(s)
s=s[1:len(s)-1]
l=s.split(",")
for i in range(len(l)):
    l[i]=int(l[i])
list=[]
point=[]
sum=0
'''for i in range(len(l)):
    squart=[]
    n=l[i]
    for j in range(len(list)):
        m=max(list[j])
        if n<m:
            for k in range(j+1,len(list),1):
                list[j]=list[j]+list[k]
                sum=j
            break
    print(sum)
    print(list)
    list[sum].append(n)
    sum=sum+1
print(sum)'''
sum=1
point.append(0)
for i in range(1,len(l),1):
    flag=0
    for j in range(len(point)):
        if j==len(point)-1:
            squart=l[point[len(point)-1]:i]
            
        else:
            squart=l[point[j]:point[j+1]]
            
        if l[i]<max(squart):
            flag=1
            point=point[:j+1]
            break
        
    if flag==0:
        sum=sum+1
        point.append(l[i])
print(len(point))
            
            
    

        
