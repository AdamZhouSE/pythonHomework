def iii(i):
    if i == 1 or i ==2 or i == 3 or i == 5:
        return i
    elif i%2 == 0:
        return i/2
    elif i%3 == 0:
        return i/3
    elif i%5 == 0:
        return i/5
    else:
        return i
        
a = int(input())
for i in range(7,a):
    sign = True
    if a%iii(i) != 0:
        sign = False
print(sign)    
        