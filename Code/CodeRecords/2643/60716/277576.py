str1 = input().split(',')
str2 = input().split(',')
magic = int(input())
customers = [int(i) for i in str1]
grumpy = [int(i) for i in str2]
maxcus = 0
for i in range(len(grumpy)):
    temp = 0
    for t in range(len(customers)):
        if grumpy[t]==0:
            temp+=customers[t]
        elif grumpy[t] ==1 and (t>=i and t<=i+magic):
            temp +=customers[t]
        else:
            temp+=0
    if temp>maxcus:
        maxcus = temp
print(maxcus)