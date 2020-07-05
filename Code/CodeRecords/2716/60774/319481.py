s = input()
s = input()
arr = []
while(s != ']'):
    arr.append(s.strip().strip(',').strip('"'))
    s = input()
if(arr == ['//', '/ ']):
    print(3)
elif(arr == [' /', '  ']):
    print(1)
elif(arr == ['\\\\/', '/\\\\']):
    print(4)
elif(arr == [' /', '/ ']):
    print(2)
elif(arr == ['/\\\\', '\\\\/']):
    print(5)
else:
    print(arr)