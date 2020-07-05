n=int(input())
list2=[]
sum=1
for i in range(n):
    list1=input().split()
    tt=int(list1[0])*60+int(list1[1])
    if tt not in list2:
        list2.append(tt)
    else:
        sum+=1
print(sum)

    
