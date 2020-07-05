def intToBinary(n):
    str=""
    while n>0:
        rem=n%2
        n=n//2
        if rem==1:
            str="1"+str
        else:
            str="0"+str
    count=len(str)
    if count<8:
        for i in range(count,8):
            str="0"+str
    return str

num=int(input())
for i in range(0,num):
    n,m=map(int,input().split())
    pos=-1
    str1=intToBinary(n)
    str2=intToBinary(m)
    for j in range(0,8):
        if str1[7-j]!=str2[7-j]:
            pos=j+1
            break
    print(pos)