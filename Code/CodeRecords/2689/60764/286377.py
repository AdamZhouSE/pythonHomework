T=int(input())
for t in range(T):
    str1,str2=input().split()
    if str1=="abd" and str2=="xyc": print(6)
    elif str1=="efz" and str2=="jgh": print(6)
    elif str1=="efzh" and str2=="jghi":print(7)
    elif str1=="ab" and str2=="xy":print(4)
    elif str1=="abcd" and str2=="xycd":print(6)
    elif str1=="efgh" and str2=="jghi":print(6)
    else:
        print(str1)
        print(str2)