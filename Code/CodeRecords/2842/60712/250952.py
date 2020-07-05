n = int(input())
employees = [0]*n
for i in range(n):
    employees[i]=int(input())
max1 = 0
for i in range(n):
    temp = 1
    k=i
    for j in range(0,n):
        if employees[k]!=-1:
            temp+=1
            k = employees[k]-1
        else:
            if temp>max1:
                max1=temp
            break
print(max1)
            
    