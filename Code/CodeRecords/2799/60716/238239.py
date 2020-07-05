number = int(input())
str = input().split(' ')
price = [int(i) for i in str]
price.sort()
check = True
for i in range(number):
    if i+1 == number:
        break
    index1=price[i]
    index2=price[i+1]
    if index2%index1!=0:
#        print("True")
        while index2%2==0:
            index2 = index2//2
        while index2%3==0:
            index2 = index2//3
        while index1%2==0:
            index1 = index1//2
        while index1%3==0:
            index1 = index1//3
        if index2%index1!=0 or index1%index2!=0:
            check = False
    else:
        index = index2//index1
        while index%2==0:
            index = index//2
        while index%3==0:
            index = index//3
        if index!=1:
            check = False
print("Yes") if check else print("No")