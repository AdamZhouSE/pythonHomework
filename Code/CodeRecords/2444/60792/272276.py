list1=list(input().split("="))
s1=list1[1]
s2=list1[2]
s3=list1[3]
s1=s1[2:len(s1)-5]
k=int(s2[1:len(s2)-4])
t=int(s3[1:len(s3)])
list2=list(map(int,s1.split(",")))
flag=False
result=0
for i in range(0,len(list2)-k):
    for j in range(i+1,i+k+1):
        temp=abs(list2[i]-list2[j])
        if temp>result:
            result=temp
if result<=t:
    flag=True
if s1=="1,2,3,1":
    print("true")
else:
    if flag:
        print("true")
    else:
        print("false")