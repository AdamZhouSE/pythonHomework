num = int(input())
test =[]

for i in range(num):
    test.append(input())

for i in range(num):
    temp = test[i]
    if int(temp)%5 :
        print("NO")
    else:
        print("YES")
        