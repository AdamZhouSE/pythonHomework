num = input().split(",")
res = 0 
sum = 0
for i in num:
    sum = sum + int(i)
for i in num:
    res = res + abs(int(i)-round(sum/len(num)))
print(res)