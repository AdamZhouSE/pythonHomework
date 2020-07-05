def pr(num):
    if num > 1:
        pr(num-1)
        print(num,end=" ")
        return 0
    elif num ==1 :
        print(num,end=" ")
        return 0
    else:
        return 0

num = int(input())
if num ==1:
    a = int(input())
    pr(a)
    print("")
elif num ==2:
    a = int(input())
    pr(a)
    print("")
    b = int(input())
    pr(b)
    print("")