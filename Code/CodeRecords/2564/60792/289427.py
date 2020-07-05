s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
k=int(input())
x=int(input())
list2=[]
len1=len(list1)
left=0
right=len1-1
while len1>k:
    if abs(list1[left]-x)>abs(list1[right]-x):
        left+=1
    else:
        right-=1
    len1-=1
for i in range(left,right+1):
    list2.append(list1[i])
print(list2)    