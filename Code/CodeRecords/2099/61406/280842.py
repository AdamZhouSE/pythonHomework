source = input()
if len(source)>1:
    a = ord(source[0])-ord('A')+1
    b = ord(source[1])-ord('A')+1
else:
    a = 0
    b = ord(source[0])-ord('A')+1
n = a*26+b
print(n)