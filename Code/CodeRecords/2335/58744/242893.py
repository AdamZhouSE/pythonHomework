str_var = input()
str_x, str_y = str_var.split(', ')
x, y = int(str_x.split(' = ')[1]), int(str_y.split(' = ')[1])

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
