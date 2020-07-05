string = input()

boy = 0
girl = 0
for m in range(len(string)):
    if((string[m]=='b') or(m + 1 <len(string) and string[m+1] == 'o') or(m + 2 <len(string) and string[m+2] == 'y')):
        boy = boy + 1
    if((string[m]=='g') or (m + 1 <len(string) and string[m+1] == 'i') or (m + 2 <len(string) and string[m+2] == 'r') or (m + 3 <len(string) and string[m+3] == 'l')):
        girl = girl + 1

print(boy)
print(girl,end = "")
