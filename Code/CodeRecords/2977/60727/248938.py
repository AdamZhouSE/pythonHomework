while True:
    data = input()
    if data=='!':
        break
    else:
        for i in data:
            if(i>'A' or i=='A' )and(i<'Z' or i=='Z'):
                print(chr(ord('Z')-(ord(i)-ord('A'))),end='')
            elif(i>'a' or i=='a' )and(i<'z' or i=='z'):
                print(chr(ord('z')-(ord(i)-ord('a'))),end='')
            else:
                print(i,end='')
        print()