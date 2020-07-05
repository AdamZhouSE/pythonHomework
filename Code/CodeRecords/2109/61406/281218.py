source = input()
sum = 0
while True:
    for i in source:
        sum = sum+int(i)
    if sum<10:
        break
    source = str(sum)
    sum = 0
print(sum)