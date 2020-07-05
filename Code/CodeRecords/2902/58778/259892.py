str1=input("")
x=int(str1)
i=1
while i<=x:
    #打印每一行
    for y in range(0,int((x-i)/2)):
        print('*',end='')
    for y in range(0,i):
        print("D",end='')
    for y in range(0,int((x-i)/2)):
        print('*',end='')
    print("")
    i=i+2
i=x-2
while i>=1:
    for y in range(0,int((x-i)/2)):
        print('*',end='')
    for y in range(0,i):
        print("D",end="")
    for y in range(0,int((x-i)/2)):
        print("*",end='')
    print('')
    i=i-2