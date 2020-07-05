start=int(input())
end=int(input())
list=[]
jud=True
temp=0
for i in range(start,end+1):
    temp=i
    jud=True
    while temp!=0:
        if temp%10==0:
            jud=False
            break
        elif i%(temp%10)!=0:
            jud=False
            break
        temp=temp//10
    if jud:
        list.append(i)
print(list)