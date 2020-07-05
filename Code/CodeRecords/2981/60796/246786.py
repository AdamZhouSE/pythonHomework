def reverse(substring):
    i=len(substring)-1
    s=""
    while i>=0:
        s=s+substring[i]
        i=i-1
    return s

n = input().split("  ")
n = [int(x) for x in n]
P1 = n[0]
P2 = n[1]
P3 = n[2]
s = input()
#print(n)
#print(s)
# 下面处理“-”：用“~”来表示连接数字的“-”,用“=”来表示连接字母的“-”:
for i in range(1, len(s) - 1):
    if s[i] == '-':
        if (s[i + 1].isdigit() and s[i - 1].isdigit()):
            s = s[:i] + "~" + s[i + 1:]
        if s[i - 1].isalpha() and s[i + 1].isalpha():
            s = s[:i] + "=" + s[i + 1:]

# 下面进行填充：
i = 0
while i <= len(s) - 2:
    if s[i] == '=':  # 下面填充字母
        if ord(s[i - 1]) + 1 == ord(s[i + 1]):
            s = s[:i] + s[i + 1:]  # 删掉“=”
        else:
            string = ""
            for j in range(ord(s[i - 1]) + 1, ord(s[i + 1])):
                string=string+chr(j)*P2
            if P1==1:
                string=string.lower()
            elif P1==2:
                string=string.upper()
            elif P1==3:
                string="*"*len(string)
            if P3==2:
                string=reverse(string)
            s=s[:i]+string+s[i+1:]
    elif s[i]=='~':   #下面填充数字
        if ord(s[i - 1]) + 1 == ord(s[i + 1]):
            s = s[:i] + s[i + 1:]  # 删掉“=”
        else:
            string = ""
            for j in range(ord(s[i - 1]) + 1, ord(s[i + 1])):
                string=string+chr(j)*P2
            if P1==3:
                string="*"*len(string)
            if P3==2:
                string=reverse(string)
            s=s[:i]+string+s[i+1:]
    i=i+1
    
print(s)






