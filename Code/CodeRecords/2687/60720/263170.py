size=int(input())
def findx(n):
    flag=0
    str1='10'
    print(1,end='')
    while(sum(str1)<=n):
        print(' ',end='')
        if str1!='0':
            print(sum(str1),end='')
        if flag==1:
            str1=str1+'0'
            flag=0
        else:
            str1=str1+'1'
            flag=1
def sum(str0):
    result=0
    for i in range(len(str0)):
        result+=int(str0[i])*pow(2,len(str0)-i-1)
    return result
for k in range(size):
    n=int(input())
    findx(n)
    print()