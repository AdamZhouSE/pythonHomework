num = int(input())
test =[]

for i in range(num):
    test.append(input())

for i in range(num):
    al=test[i].split(' ')
    a = int(al[0],2)
    b = int(al[1],2)
    print(a*b)