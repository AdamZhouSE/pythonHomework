number = int(input())
str = input().split(' ')
price = [int(i) for i in str]
#price.sort()
check = True
for i in range(number):
    if i+1 == number:
        break
    index1=price[i]
    index2=price[i+1]
    if index2%index1!=0:
        check = False
        break
    else:
        index = index2//index1
        while index%2==0:
            index = index//2
        while index%3==0:
            index = index//3
        if index!=1:
            check = False
print("YES") if check else print("NO")