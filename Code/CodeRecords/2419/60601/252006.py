num = list(map(int,list(input())))
mul = 1
add = 0
for i in num:
    mul = mul * i
    add = add + i
print(mul-add)
           