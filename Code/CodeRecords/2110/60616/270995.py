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
        elif num % 5 == 0:  
            num = num // 5  
        else: 
            return False  
num=int(input())
print(isUgly(num))