a = list(eval(input()))
even = []
odd = []
num = []
for i in a:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
odd.sort()
even.sort()
for i in range(odd.__len__()):
    num.append(even[i])
    num.append(odd[i])
print(num) 