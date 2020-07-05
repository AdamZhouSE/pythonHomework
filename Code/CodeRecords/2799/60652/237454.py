def GCD(a, b):
    a, b = (a, b) if a >= b else (b, a)
    while b:
        a, b = b, a % b
    return a


def hasRemainder(a):
    while a > 0:
        if a % 2 == 0:
            a = int(a / 2)
        else:
            break
    while a > 0:
        if a % 3 == 0:
            a = int(a / 3)
        else:
            break
    if a != 1:
        return False
    else:
        return True


def isEqual(a, b):
    n1 = int(a / GCD(a, b))
    n2 = int(b / GCD(a, b))
    if hasRemainder(n1) and hasRemainder(n2):
        return True
    else:
        return False


n=int(input())
arr=list(map(int,input().split()))
fp=arr[0]
outcome="Yes"
for i in range(1,len(arr)):
    if isEqual(fp,arr[i]):
        continue
    else:
        outcome="No"
        break
print(outcome)