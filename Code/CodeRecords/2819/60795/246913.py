n=int(input())
arr=raw_input()
list=[int(n) for n in arr.split(' ')]
one,two,three,four,r,re=0,0,0,0,0,0
for i in range(0,len(list)):
    if list[i]==1:
        one=one+1
    elif list[i]==2:
        two=two+1
    elif list[i]==3:
        three=three+1
    else:
        four=four+1
car=four
while three>0:
    if one>0:
        three=three-1
        one=one-1
        car=car+1
    else:
        three=three-1
        car=car+1
if two>0:
    r=car%2
    car=car+(two-r)//2
    if r==1:
        if one>1:
           one=one-2
           car=car+1
        elif one==1:
            one=one-1
            car=car+1
        else:
            car=car+1
if one>0:
    re=one%4
    car=car+(one-re)//4
    if re>0:
        car=car+1
print(car)