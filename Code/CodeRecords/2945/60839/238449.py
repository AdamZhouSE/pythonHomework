s=list(input())
boy_num=0
girl_num=0
for i in range(0,len(s)):
    if s[i]=="b":
        boy_num=boy_num+1
    if not i==0:
        if not s[i-1]=="b" and s[i]=="o":
            boy_num = boy_num + 1
        if not s[i-1]=="o" and s[i]=="y":
            boy_num = boy_num + 1
    if s[i]=="g":
        girl_num=girl_num+1
    if not i==0:
        if not s[i-1]=="g" and s[i]=="i":
            girl_num = girl_num + 1
        if not s[i-1]=="i" and s[i]=="r":
            girl_num = girl_num + 1
        if not s[i-1]=="r" and s[i]=="l":
            girl_num = girl_num + 1
print(boy_num)
print(girl_num,end="")