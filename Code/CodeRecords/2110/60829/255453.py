a=int(input())
while a>1:
    if a%2==0:
        a=a//2
    elif a%3==0:
        a=a//3
    elif a%5==0:
        a=a//5
    else:
        print("False")
        break
if a==1:
    print("True")