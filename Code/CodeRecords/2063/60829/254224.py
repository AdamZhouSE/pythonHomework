num=int(input())
str1=''
if num<10:
    print(True)
else:
    while num > 0:
        str1 = str1 + str(int(num % 10))
        num = (num - num % 10) / 10
    count = 1
    for i in range(0, int(len(str1) / 2)):
        if str1[i] == str1[len(str1) - 1 - i]:
            pass
        else:
            print('False')
            count = 0
    if count == 1:
        print('True')