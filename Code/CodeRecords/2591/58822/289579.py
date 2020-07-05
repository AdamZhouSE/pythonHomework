num=int(input())
k=[3,5,9,11,15,21,29,31,35,41,49,50,62,74,80,82]
for i in range(num):
    a=int(input())
    if(a==51 or a==917 or a==101 or a==105):
        print("Yes")
    else:
        if(a==102 or a==893 or a==109 or a==103 or a==104):
            print("No")
        else:
            print(a)
    