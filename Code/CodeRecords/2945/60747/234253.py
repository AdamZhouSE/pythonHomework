s=input()
boy=0
girl=0
for i in range(len(s)):
    if s[i] == 'b' or i+1 < len(s) and s[i+1] == 'o' or i+2 < len(s) and s[i+2] == 'y':
        boy=boy+1
    if s[i] == 'g' or i+1 < len(s) and s[i+1] == 'i' or i+2 < len(s) and s[i+2] == 'r' or i+3 < len(s) and s[i+3] == 'l':
        girl = girl + 1
print(boy)
print(girl,end='')