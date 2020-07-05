list1=eval(input())
count=[0]*len(list1)
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            count[i]+=1
print(count)