n=input()
x=input()
a=x.split(" ")
#print(a)

i=1
num=0
num2=0
while i<len(a)-1:
    if(a[i-1]=='1' and a[i+1]=='1'):
        a[i+1]='0'
        num+=1
    i=i+1
    
a=x.split(" ")
i=len(a)-2
while i>0:
    if(a[i-1]=='1' and a[i+1]=='1'):
        a[i-1]='0'
        num2+=1
    i=i-1

if(num<num2):
    print(num)
else:
    print(num2)