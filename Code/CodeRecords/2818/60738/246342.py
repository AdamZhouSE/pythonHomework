list1=input().split(" ")
list2=input().split(" ")
list3=[]
n=int(list1[0])
x=int(list1[1])
time=0
for num in range(n):
    list3.append(int(list2[num]))
list3.sort()
for i in range(n):
    if(x>=1):
        time+=list3[i]*x
        x-=1
    else:
        time+=list3[i]*1
print(time)
    


