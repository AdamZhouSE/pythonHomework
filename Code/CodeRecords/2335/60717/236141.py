x=int(input())
y=int(input())

if x>y:
    flag=1
else:
    flag=0
    
count=0

while x < y:
    x=x*2
    count+=1

output=x-y+count

if (x-y)%2==0and flag==0:
    output-=(x-y)/2
elif(x-y)%2==1and flag==0:
    output-=(x-y-1)/2

print(int(output))    
