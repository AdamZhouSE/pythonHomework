def IsCrossing(num):
    if num[0]>=num[2] and num[3]>=num[1]:
        return True
    return False
num=list(map(int,input().split(',')))
print(IsCrossing(num))