a = list(input())
b = list(input())
num = 0
for i in range(a.__len__()-b.__len__()+1):
    for j in range(b.__len__()):
        if a[i+j] != b[j]:
            break
        if j == b.__len__()-1:
            num += 1
print(str(num),end="")            