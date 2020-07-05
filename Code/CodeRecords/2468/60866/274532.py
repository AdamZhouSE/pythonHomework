def shuzu(a):
    ans=''
    num=1
    for i in range(0,len(a)):
        num=num*a[i]
    for x in a:
        ans=ans+str(num//x)+' '
    return ans
count=int(input())
for i in range(0,count):
    meiyong=input()
    line2=input().split(' ')
    line2=[int(x) for x in line2]
    print(shuzu(line2))