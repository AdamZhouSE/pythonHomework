import collections
N=input()
a=0
counter1 = collections.Counter(str(N))        
n = len(str(N))        
num = 1        
while len(str(num)) < n: num *= 2        
while len(str(num)) == n:            
    if collections.Counter(str(num)) == counter1: 
        print("true") 
        a=-1
    num *= 2  
if a!=-1:    
    print( "false")
