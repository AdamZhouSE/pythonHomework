def judge(num):
    if num==1:
        return False
    if num==2 or num==3:
        return True
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True
def countjc(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result
n=int(input())
MOD=int(pow(10,9))+7
count=0
for i in range(1,n+1):
    if judge(i):
        count=count+1
total=countjc(count)
total=total*countjc(n-count)
total=total%MOD
print(total)