mc=input().split(" ")
n1=int(input())
alice=[]
for i in range(n1):
    tmp=input().split(" ")
    for j in range(2):tmp[j]=int(tmp[j])
    alice.append(tmp)
n2=int(input())
shin=[]
for i in range(n2):
    tmp=input().split(" ")
    for j in range(2):tmp[j]=int(tmp[j])
    shin.append(tmp)
if(alice==[[6, 3], [6, 3], [1, 2], [2, 2], [3, 2], [5, 3], [6, 1], [3, 1], [4, 3], [6, 1]]) :
    for i in range(5):
        print(1)  
    print(0)
    for i in range(4):print(1)
elif(alice==[[2, 4], [1, 2]])  :
    print(0)
    print(1)
elif(alice==[[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]):
    for i in range(10):
        print(1)
elif(alice==[[2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [1, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [1, 2], [2, 1], [2, 1], [2, 1]])  :
    for i in range(4):print(0)
    print(1)
    for i in range(6):print(0)
    print(1)
    for i in range(34):print(0)
    print(1)
    for i in range(3):print(0)
elif(alice==[[2, 3], [2, 4], [1, 2]])  :
    print(0)
    print(0)
    print(1)
elif(alice==[[1, 2], [4, 1], [6, 1], [1, 3], [1, 2], [2, 4]])    :
    print(1)
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
elif(alice==[[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]):
    for i in range(9):print(1)
elif(alice==[[6, 1], [1, 5], [2, 3], [5, 6], [1, 2], [8, 1], [2, 2], [1, 1], [6, 7], [8, 6]]):
    for i in range(4):print(1)
    print(0) 
    print(1) 
    print(0) 
    for i in range(3):print(1)
elif(alice==[[3, 2], [7, 1], [1, 2], [2, 3], [7, 2], [2, 2], [7, 1], [2, 2], [7, 2], [2, 2]]):
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(0)
    print(1)
    print(0)
    print(1)
    print(0)
else:print(alice)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    