def isUgly(num):
        if num <= 0:                
            return False
        while True:                
            if num == 1:            
                return True         
            if num % 2 == 0:        
                num = num // 2      
            elif num % 3 == 0:      
                num = num // 3
            elif num%5==0:  
                num = num // 5      
            else:                   
                return False        
n=int(input())
i=1
while(n!=0):
    if(isUgly(i)):
        n-=1
    i+=1
print(i-1)