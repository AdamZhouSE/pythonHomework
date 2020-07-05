s=list(input())
boy_num=0
girl_num=0
for i in range(0,len(s)-3):
    if s[i]=="b" and s[i+1]=="o" and s[i+2]=="y":
        boy_num=boy_num+1
    if s[i]=="g" and s[i+1]=="i" and s[i+2]=="r" and s[i+3]=="l":
        girl_num=girl_num+1
if s[len(s)-3]=="b" and s[len(s)-2]=="o" and s[len(s)-1]=="y":
    boy_num=boy_num+1
print(boy_num)
print(girl_num)