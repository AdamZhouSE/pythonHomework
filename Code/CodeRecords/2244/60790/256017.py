def is_primer(num):
    return num>1 and all(num%d for d in range(2,int(num**0.5)+1))
def is_huiwen(num):
    str1=str(num)
    n=len(str1)
    if(n%2==0):
        for i in range(0,int(n/2)):
            if(str1[i]!=str1[n-i-1]):
                return False
    else:
        for i in range(0,int(n/2)):
            if(str1[i]!=str1[n-i-1]):
                return False
    return True
n=int(input())
j=n
while(True):
    if(is_huiwen(j) and is_primer(j)):
        break
    else:
        j+=1
print(j)
