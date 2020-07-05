num = int(input())
judge = False
while num!=1:
    if num%2 != 0:
        break
    num = num/2
else:
    judge = True
print(judge)