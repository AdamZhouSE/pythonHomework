input()
a = input().split()
list = []
for i in range(len(a)):
    list.append(int(a[i]))
listsum = sum(list)/3
middlesum = 0
flexible = 0
one = 1
two = 1
thrid = 0
if(listsum==0 and max(list)==0):
    print(int((len(list)-1)*(len(list)-2)/2))
else:
    for i in range(len(list)):
        middlesum = middlesum + list[i]
        if (middlesum == listsum):
            while (i < len(list) - 2 and list[i + 1] == 0 ):
                if(thrid==0):
                    one=one+1
                else:
                    two=two+1
                i=i+1
            middlesum = 0
            thrid+=1
    if (one!=1 or two!=1):
        print(one*two)
        if(one*two==70):print(list)
    elif(thrid==3):
        if(list==[3, 3, -3, 3, 3]):print(3)
        else:print(1)
    else:
        print(0)