s = input()
boy = 0
girl = 0

for i in range(len(s)):
    if s[i] == 'b':
        boy = boy + 1
    if s[i] == 'o' and s[i-1] != 'b':
        boy = boy + 1
    if s[i] == 'y' and s[i-1] != 'o':
        boy = boy + 1
    if s[i] == 'g':
        girl = girl + 1
    if s[i] == 'i' and s[i-1] != 'g':
        girl = girl + 1
    if s[i] == 'r' and s[i-1] != 'i':
        girl = girl + 1
    if s[i] == 'l' and s[i-1] != 'r':
        girl = girl + 1

print(boy)
print(girl,end="")