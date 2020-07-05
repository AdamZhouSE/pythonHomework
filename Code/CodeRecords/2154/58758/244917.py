num = input()
flag = True
for i in range(0, len(num)//2):
    if num[i] != num[len(num)-i-1]:
        flag = False
        break
print(flag)
