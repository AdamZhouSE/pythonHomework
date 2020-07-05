
num = int(input())
rs=9
r=10
for i in range(2,num+1):
    rs=rs*(10-i+1)
    r+=rs
print(r)