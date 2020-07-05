def findsquarenumber(num):
    i=1
    while num>=i*i:
        if num<(i+1)*(i+1):
            return i
def judge(num):
    if(num==0):
        return True
    squarenumber=findsquarenumber(num)
    for h in range(1,squarenumber):
        for k in range(1, squarenumber):
            if num==h*h+k*k:
                return True
    return False
num=int(input())
print(judge(num))