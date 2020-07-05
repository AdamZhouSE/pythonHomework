num = int(input())
index = 0
for i in range(num+1):
    for j in range(num+1):
        if (i+j)*(i-j+1)//2==num:
            index+=1
print(index)