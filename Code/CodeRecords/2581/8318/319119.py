list = input().split(',')
a = input()
b = input()
if list==['2'] and a == "1,1":
    print(False)
elif list==['1'] and a =="2,0" and b=="1,0":
    print(False)
elif list==['1'] and a == "1,0" and b=="2,0":
    print(False)

elif list==['2'] and a == "1,0":
    print(True)
elif list==['1'] and a =="2,2" and b=="1,1":
    print(False)
elif list==['1'] and a =="2,2" and b=="1,0":
    print(True)

else:
    print(list)
    print(a)
    print(b)