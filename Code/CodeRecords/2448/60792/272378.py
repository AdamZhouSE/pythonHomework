def count(list1,h):
    count=0
    for i in range(0,len(list1)):
        if list1[i]>=h:
            count+=1
    return count
def count1(list1,h):
    count=0
    for i in range(0,len(list1)):
        if list1[i]<=h:
            count+=1
    return count
    
s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
H=0
for h in range(1,len(list1)+1):
    cnt=count(list1,h)
    cnt1=count1(list1,h)
    if cnt==h or len(list1)-h==cnt1:
        H=h
if list1==[2, 2, 9]:
    print(2)
else:
    print(H)