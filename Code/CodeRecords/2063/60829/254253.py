num=int(input())
if num<10 and num>-1:
    print(True)
else:
    str1=str(num)
    count=1
    for i in range(0, int(len(str1) / 2)):
        if str1[i] == str1[len(str1) - 1 - i]:
            pass
        else:
            print('False')
            count = 0
            break
    if count == 1:
        print('True')