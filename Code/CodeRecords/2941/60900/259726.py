n = int(input())
str = input()
count = 0
for i in range(0,len(str)):
    if str[i]=='A':
        count+=4
    elif str[i]=='B':
        count+=3
    elif str[i]=='C':
        count+=2
    elif str[i]=='D':
        count+=1
    elif str[i]=='F':
        count+=0
a=count/n

final = "{:.14f}".format(a)


if count !=0:
    print(final,end='')
else:
    print("0",end='')