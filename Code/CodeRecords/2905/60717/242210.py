list1=(eval(input()))

e=len(list1)-1

summ=0

for i in list1:
    summ+=i*(2**e)
    e-=1

print(summ)