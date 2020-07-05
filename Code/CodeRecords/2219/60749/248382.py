def findsquarenumber(num):
    i=1
    while num>=i*i:
        if num<=(i+1)*(i+1):
            return i
        i+=1
def judge(num):
    if(num==0):
        return True
    squarenumber=findsquarenumber(num)
    for h in range(0,squarenumber):
        for k in range(0, squarenumber):
            if num==h*h+k*k:
                return True
    return False
num=int(input())
print(judge(num))