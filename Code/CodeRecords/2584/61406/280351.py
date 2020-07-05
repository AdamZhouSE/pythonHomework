def nim(x):
    if x%4==0:
        return False
    else:
        return True
    
    
n = int(input())
print(nim(n))