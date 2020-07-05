a=int(input())
b=''.join(input().split()).split(',')
index=int(''.join(map(str,b)))
rs=1
for i in range(index):
    rs=rs*a
print(rs%1337)




