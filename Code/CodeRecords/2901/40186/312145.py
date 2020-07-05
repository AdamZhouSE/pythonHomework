inp = int(input())
if bin(inp).find('11') or bin(inp).find('00'):
    print('False')
else:
    print('True')