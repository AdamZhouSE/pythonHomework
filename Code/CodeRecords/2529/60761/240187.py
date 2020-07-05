n=input("")
bits=len(n)
values=[]
if bits%3==1:
    exponents=[int((bits-1)/3)*10+value for value in range(0,4)]
elif bits%3==2:
    exponents=[int((bits-1)/3)*10+value for value in range(4,7)]
else:
    exponents=[int((bits-1)/3)*10+value for value in range(7,10)]
for exponent in exponents:
    values.append(str(2**exponent))
for value in values:
    result="true"
    for letter in n:
        if letter not in value:
            result="false"
    if result=="true":
        break
print(result)
        