a=input()
rs=0
index=1
for aa in range(len(a)):
    aaa=a[len(a)-aa-1]
    rs=rs+(ord(aaa)-ord('A')+1)*index
    index*=26
print(rs)