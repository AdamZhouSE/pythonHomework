num=int(input())
for i in range(0,num):
    if i*i==num:
        print(True)
        break
    elif i*i>num:
        print(False)
        break