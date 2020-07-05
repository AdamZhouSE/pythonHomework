N=int(input())
for n in range(0,N):
    tempstr=input()
    str=""
    for item in tempstr:
        if (item.isalpha()):
            str=str+item.lower()
    l=len(str)
    half=int((l+0.75)/2)
    str1=str[0:half+1]
    str2=str[half:]
    l = list(str2)
    l.reverse()
    str2 = "".join(l)
    if(str1==str2):
        print("YES")
    else:
        print("YES")
