num=int(input())
if num==0:
    print("False")
else:
    while num%3==0:
        num=num/3
    if num==1:
        print("True")
    else:
        print("False")