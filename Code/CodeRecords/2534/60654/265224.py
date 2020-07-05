a = list(input())
b = []
for i in a:
    if '0'<=i <='9':
        b.append(int(i))
b.sort()        
print(b)        
