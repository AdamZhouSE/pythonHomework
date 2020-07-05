def finder(str1,str2):
    num=0
    loc=str1.find(str2[0])
    if len(str2)==1:
        while loc!=-1:
            num=num+1
            loc=str1.find(str2[0],loc+1)
        return num
    while loc!=-1:
        num=num+finder(str1[loc+1:len(str1)],str2[1:len(str2)])
        loc=str1.find(str2[0],loc+1)
    return num

t=int(input())
for i in range(0,t):
    n,m=map(int,input().split(' '))
    str1,str2=map(str,input().split(' '))
    print(finder(str1,str2))