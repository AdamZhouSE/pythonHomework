res=0
for i in range(-2,3):
    row=input().split()
    if("1" in row):
        res+=abs(row.index("1")-2)
        res+=abs(i)
        break;
print(res)