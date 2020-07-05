input()
a = input().split()
list = []
for i in range(len(a)):
    list.append(int(a[i]))
listsum = sum(list)/3
middlesum = 0
flexible = 0
thrid = 0
if(listsum==0 and max(list)==0):
    print(int((len(list)-1)*(len(list)-2)/2))
    #if(int((len(list)-1)*(len(list)-2)/2)==3):print(list)
else:
    for i in range(len(list)):
        middlesum = middlesum + list[i]
        if (middlesum == listsum):
            if (i < len(list) - 2 and list[i + 1] == 0 and i != 0):
                flexible += 1
            else:
                middlesum = 0
                thrid = thrid + 1
    #if(flexible==2):print(list)
    if (thrid == 3):
        print(flexible + 1)
    else:
        print(0)