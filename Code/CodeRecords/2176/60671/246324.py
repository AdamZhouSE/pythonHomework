str=input();list=[];i=1
for c in str:
    list.append(c+"%d"%(i))
    i+=1
list.sort()
len=len(str)
list1=[]
for c in list:
    list1.append(len+1-int(c[1]))
j=0
while j<len-1:
    print(list1[j],end=' ')
    j+=1
print(list1[len-1])    
    

    