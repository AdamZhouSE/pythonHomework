size=int(input())
for k in range(size):
    n=int(input())
    str1=''
    for i in range(n):
        str1+='0'
    while(n>9):
        str1='9'+str1
        n-=9
    str1=str(n)+str1
    print(str1)