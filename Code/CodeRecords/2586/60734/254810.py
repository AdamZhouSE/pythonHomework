x = int(input())
y = int(input())
z = int(input())

min_steps = 0
max_steps = 0
if y>x+1:
    min_steps += 1
    max_steps += (y-x-1)

if z>y+1:
    min_steps+=1
    max_steps += (z-y-1)
    
print([min_steps,max_steps])