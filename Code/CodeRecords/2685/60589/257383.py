t=int(input())
for i in range(t):
    n=int(input())
    pos='0'*n
    pre=''
    while n>9:
        n-=9
        pre+='9'
    pre=str(n)+pre
    print(pre+pos)