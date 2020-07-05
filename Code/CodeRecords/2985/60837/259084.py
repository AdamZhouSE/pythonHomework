def findLeftAndRight(num):
    if num==1:
        return "A"
    return findLeftAndRight(num-1)+chr(ord("A")+num-1)+findLeftAndRight(num-1)

n=int(input())
print(findLeftAndRight(n))