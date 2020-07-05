import math

result=[]
x=int(input())
y=int(input())
bound=int(input())
for k in range(1,bound+1):
    for i in range(math.floor(math.log(k,x))):
        if type(math.log(k-math.pow(x,i),y))==int:
            print(k)          
        
    
    
      
     