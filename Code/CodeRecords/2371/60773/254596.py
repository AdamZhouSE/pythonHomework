def check(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


num = int(input())
dic={
    'A':'a',
    'B':'b',
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'H': 'h',
    'I': 'i',
    'J': 'j',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'O': 'o',
    'P': 'p',
    'Q': 'q',
    'R': 'r',
    'S': 's',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'X': 'x',
    'Y': 'y',
    'Z': 'z',
}
for k in range(num):
    s = input()
    str = ""
    for i in range(len(s)):
        if(s[i]<='Z' and s[i]>='A'):
            str=str+dic[s[i]]
        elif s[i]<='9' and s[i]>='0':
            str=str+s[i]
        elif s[i]<='z' and s[i]>='a':
            str=str+s[i]
        else:
            str=str
    if check(str):
        print("YES")
    else:
        print("NO")