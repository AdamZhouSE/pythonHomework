import math

result=[]
x=int(input())
y=int(input())
bound=int(input())
print(x)
print(y)
print(bound)
for k in range(2,bound+1):
    for i in range(0,math.ceil(math.log(k,x))):
        print(math.log(k-math.pow(x,i),y),k)
               
        
    
      
     