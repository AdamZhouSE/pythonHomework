N = input()
isNumber = False
lst = sorted(list(map(int,str(N))))  
#几位数
lenofN = len(lst)

numbers = []
base = 0
number = 1
while number<10**lenofN:
    if number > (10**(lenofN-1)):
        numbers.append(number)
    number = 2**base
    base+=1
    
for x in numbers:
    res = sorted(list(map(int,str(x))))
    if res == lst:
        isNumber = True
        break

if N ==1:
    isNumber = True
if isNumber:
    print('true')
else:
    print('false')