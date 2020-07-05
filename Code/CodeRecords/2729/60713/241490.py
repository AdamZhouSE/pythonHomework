a = input()
b = len(a)
a = a[1:b-1].split(",")
i = 0
while( a[i] == a[i+1] ):
    i = i + 2
print(a[i])