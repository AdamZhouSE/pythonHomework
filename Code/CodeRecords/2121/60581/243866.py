str = int(input())

count = 0
for i in range(0,pow(10,str)):
    word = []
    number = i
    while number > 10:
        word.insert(0,number%10)
        number = int(number/10)
    word.insert(0,number)
    if word.count(0)<=1 or word.count(1)<=1 or \
            word.count(2)<=1 or word.count(3)<=1 or \
            word.count(4)<=1 or word.count(5)<=1 or \
            word.count(6)<=1 or word.count(7)<=1 or \
            word.count(8)<=1 or word.count(9)<=1:
        count += 1
print(count)