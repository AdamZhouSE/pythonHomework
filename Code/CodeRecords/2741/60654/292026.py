a = list(eval(input()))
max = 1
num = 1
for i in range(a.__len__()-1):
    if a[i] <a[i+1]:
        num+= 1
    else:
        num = 0
    if num > max:
        max = num
print(max)        