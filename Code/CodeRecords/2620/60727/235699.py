num = int(input())
for i in range(0,num):
    sum = 0
    ran = int(input())
    for j in range(1,ran+1):
        sum = pow(j,5)+sum
    print(sum)