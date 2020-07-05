a=input()
length=len(a)
if a[0]=='-':
    print('-',end="")
    if a[length-1]=='0':
        print("")
    else:
        print(a[length-1],end="")
    for i in range(2,length):
        print(a[length-i],end="")
else:
    if a[length-1]=='0':
        print("",end="")
    else:
        print(a[length-1],end="")
    for i in range(1,length):
        print(a[length-1-i],end="")
print("")