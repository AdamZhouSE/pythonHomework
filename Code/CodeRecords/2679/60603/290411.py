testnum=int(input())
for i in range(testnum):
    num=int(input())
    if(num==0):
        print(0)
    elif(num==1):
        print(3)
    elif(num==2):
        print(8)
    elif(num==3):
        print(19)
    else:
        print(int(num+num+num*(num-1)+num*(num-1)*(num-2)/2+1+num*(num-1)/2))