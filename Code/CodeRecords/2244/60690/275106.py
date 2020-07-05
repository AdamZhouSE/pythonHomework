n=int(input())
def isHW(str):
    for i in range(len(str)):
        if str[i]!=str[len(str)-1-i]: return False
    return True

def isSS(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True

while isHW(str(n))==False or isSS(n)==False: n+=1
print(n)