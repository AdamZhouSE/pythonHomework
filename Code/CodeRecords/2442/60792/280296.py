s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
list1.sort()
max=0
for i in range(0,len(list1)-1):
    if list1[i+1]-list1[i]>max:
        max=list1[i+1]-list1[i]
print(max)