def sumup(a,b,numbers):
    if b == 1:
        if a not in numbers:
            return 1
        else:
            return 0 
    for i in range(1,a):
        if i not in numbers:
            numbers.append(i)
            if sumup(a-i,b-1,numbers):
                return 1
            numbers.pop()
    return 0
    

t = int(input())
test = []
for i in range(t):
    test.append(list(map(int,input().split(' '))))
for x in test:
    a,b = x[0],x[1]
    print(sumup(a,b,[]))