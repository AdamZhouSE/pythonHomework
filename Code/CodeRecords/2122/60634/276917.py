x = int(input())
y = int(input())
z = int(input())
print(z%x==0 or z%y==0 or z%abs(x-y)==0)