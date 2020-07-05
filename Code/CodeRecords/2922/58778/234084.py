n=int(input())
str=input()
list1=str.split( )
temp=[]
for i in list1:
    temp.append(int(i))
ma=max(temp)
mi=min(temp)
x=int((ma-mi)/2)
y=mi+x
j=0

for i in temp:
    if(abs(i-y)==0 or abs(i-y)==x):
        k=1
    else:
        j=1
        break;
if j==1:
    print("NO")
else:
    print("YES")