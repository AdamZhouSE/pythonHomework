inp = int(input())
if bin(inp).find('11')==-1 and bin(inp).find('00')==-1:
    print('True')
else:
    print('False')