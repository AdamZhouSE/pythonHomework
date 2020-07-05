a=eval(input())
list1=[]
count=0
for i in range(a):
    b=input()
    temp=list(b)
    temp.sort()
    if(temp not in list1):
        list1.append(temp)
        count+=1
print(count,end='')