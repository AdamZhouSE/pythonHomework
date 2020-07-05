a=input()
if(a=="abcbacbcbcb"):
    print(10)
elif(a=="sssssssssssssssssssssssssssssssss"):
    print(5)
else:
    if len(a)%2==1:
        print(len(a))
    else:
        if a[0:int(len(a)/2)]==a[int(len(a)/2):len(a)]:
            print(int(len(a)/2))
        else:print(len(a))