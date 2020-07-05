str=input()
num=0
see=set()
see.add(str)
while True:
    for s in str:
       num=num+int(s)*int(s)
    if num==1:
        print(True)
        break
    str ="%d"%num
    if str not in see:
        see.add(str)
    else:
        print(False)
        break
    num=0