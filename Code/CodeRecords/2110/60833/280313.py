num=int(input())
if num <= 0:                
    print("False")
else:
    while True:                 
        if num == 1:            
            print("True")
            break
        else:
            if num % 2 == 0:        
                num = num // 2      
            elif num % 3 == 0:      
                num = num // 3      
            elif num % 5 == 0:      
                num = num // 5      
            else:                   
                print("False")
                break
    