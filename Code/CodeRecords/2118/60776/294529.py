a=int(input())
if(a==0):
    print("False")
else:
    result = "True"
    while (True):
        if (a == 1):
            break
        else:
            if (a % 3 != 0):
                result = "False"
                break
            else:
                a = int(a / 3)
    print(result)