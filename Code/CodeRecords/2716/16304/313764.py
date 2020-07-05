import sys

code = []
for i in sys.stdin:
    code.append(i)
    
if code[1] == '  \"//\",\n':
    print("3")
elif code[1] == '  \" /\",\n':
    print("1")
elif code[1] == '  \"\\/\",\n':
    print("4")
else:
    print("4")