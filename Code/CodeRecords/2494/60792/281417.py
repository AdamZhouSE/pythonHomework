s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
count=0
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]*2:
            count+=1
print(count)            