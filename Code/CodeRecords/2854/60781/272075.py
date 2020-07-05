str1=input()
str1=str1.split(' ')
str1=list(map(int,str1))
pan=0
for i in range(6):
    a=str1[i]
    num=str1.count(a)
    if(num>=4):
        pan=1
        break
if(pan==0):
    print('Alien')
else:
    str1.sort()
    if(num==6):
        print('Elephant')
    if(num==5):
        print('Bear')
    if(num==4):
        if((str1[0]==str1[1] and str1[2]!=str1[1]) or (str1[3]!=str1[4] and str1[4]==str1[5])):
            print('Elephant')
        else:
            print('Bear')