def sqrt(x):
    for i in range(x):
        if i * i > x:
            return i-1

    
a = int(input())
print(sqrt(a))