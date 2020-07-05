num=int(input())
if num<0:
    print(False)
elif num<=1:
    print(True)
else:
    for i in range(2,num):
        if i**2==num:
            print(True)
            break
        elif i**2>num:
            print(False)
            break