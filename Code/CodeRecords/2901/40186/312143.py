inp = int(input())
if not(bin(inp).find('11')) and not(bin(inp).find('00')):
    print('True')
else:
    print('False')