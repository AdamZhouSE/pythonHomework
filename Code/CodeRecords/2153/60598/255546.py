num = input()
if int(num) >= 0:
    print(int(num[::-1]))
else:
    print(int("-"+str(num[1:][::-1])))
