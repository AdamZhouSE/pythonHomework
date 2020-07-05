n = int(input())
str = ""
a = c = 1
for i in range(n):
    instr = input()
    if (instr==str):
        a=a+1
    else:
        str=instr
        if(a>c):
            c=a

if(a>c):   c=a

print(c)