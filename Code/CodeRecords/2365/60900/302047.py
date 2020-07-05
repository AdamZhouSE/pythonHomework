n = int(input())
nums =[]

def turn(a):
    if a=='0':
        return 'a'
    elif a =='1':
        return 'b'
    elif a =='2':
        return 'c'
    elif a =='3':
        return 'd'
    elif a =='4':
        return 'e'
    elif a =='5':
        return 'f'
    elif a =='6':
        return 'g'
    elif a =='7':
        return 'h'
    elif a =='8':
        return 'i'
    elif a =='9':
        return 'j'

def back(a):
    if a == 'a':
        return '0'
    elif a=='b':
        return '1'
    elif a == 'c':
        return '2'
    elif a == 'd':
        return '3'
    elif a == 'e':
        return '4'
    elif a == 'f':
        return '5'
    elif a == 'g':
        return '6'
    elif a == 'h':
        return '7'
    elif a == 'i':
        return '8'
    elif a == 'j':
        return '9'

for i in range(0,n):
    a =int(input())
    num =input().split(' ')
    for j in range(0,a):
        str=""
        for m in range(0,len(num[j])):
            str+=turn(num[j][m])
        num[j]=str
    num.sort(reverse=True)
    nums.append(num)
results =[]

for i in range(0,n):
    num =nums[i]
    for j in range(0,len(num)):
        str=""
        for m in range(0,len(num[j])):
            str+=back(num[j][m])
        num[j] =int(str)
    for j in range(0,len(num)-1):
        if num[j]/num[j+1]==10:
            num[j]=int(num[j]/10)
            num[j+1] = num[j+1]*10
    for j in range(0,len(num)-1):
        print(num[j],end='')
    print(num[len(num)-1])