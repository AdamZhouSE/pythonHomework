x = int(input())
y = int(input())

def broken_calculator(src, dest):
    count = 0
    
    while dest > src:
        count += 1
        if dest % 2 == 1:
            dest += 1
        else:
            dest //= 2
        
    return count + src - dest

print(broken_calculator(x, y))
