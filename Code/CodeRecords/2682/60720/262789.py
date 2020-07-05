size=int(input())
for k in range(size):
    list0=input().split()
    n = int(list0[0])
    l=int(list0[1])
    r=int(list0[2])
    str1=''
    while n>1:
        if n%2==0:
            str1='0'+str1
            n//=2
        else:
            str1='1'+str1
            n-=1
            n//=2
    count=0
    str1='1'+str1
    list1=list(str1)
    for i in range(l-1,r):
        list1[len(str1)-i-1]='1'
    str1=''.join(list1)
    for i in range(len(str1)):
        count+=int(str1[i])*pow(2,len(str1)-i-1)
    print(count)
