A=eval(input())
num=1
for i in A:
    if num not in A:
        break
    else:
        num+=1
print(num)