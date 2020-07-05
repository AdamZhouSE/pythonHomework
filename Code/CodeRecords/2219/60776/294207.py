a=int(input())
isright="False"
for i in range(1,a):
    for j in range(1,a):
        if i*i+j*j==a:
            isright="True"
            break
        if i*i+j*j>a:
            break
    if isright=="True":
        break
print(isright)