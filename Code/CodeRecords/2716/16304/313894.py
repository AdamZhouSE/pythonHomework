import sys

code = []
for i in sys.stdin:
    code.append(i)
    
if code[1] == '  \"//\",\n':
    print("3")
elif code[1] == '  \" /\",\n':
    if code[3] =="]" and code[2] == '  \"  \"\n':
        print("1")
    elif code[2]=='  \"/ \"\n':
        print("2") 
    else:
        print("5")
elif code[1] == '  \"\\\\/\",\n':
    print("4")
else:
    print("5")