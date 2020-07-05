nums=eval(input())
numbers.sort()
i=1
while True:
    if i in numbers:
        i+=1
        continue
    else:
        result=i
        break
print(result)