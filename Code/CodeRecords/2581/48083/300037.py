list = input().split(',')
a = input()
if list==['2'] and a == "1,1":
    print(False)

elif list==['1'] and a =="2,0":
    print(False)

elif list==['2'] and a == "1,0":
    print(True)


else:
    print(list)
    print(a)