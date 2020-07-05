list=input()
a=input()
b=0
for i in list:
    if i>a:
        b=1
        print(i)
        break
if b==0:
    print(list[2])