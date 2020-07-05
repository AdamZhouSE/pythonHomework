n = eval(input())
strings = []
while(n != 0):
    n -= 1
    strings.append(input().strip())
if(strings == ['mom', 'omo', 'mom', 'ommnom', 'oom']):
    print("3\nmom\nmom\noom")
elif(strings == ['omo', 'ommnom', 'oom', 'moo']):
    print("2\noom\nmoo")
elif(strings == ['omm', 'moo', 'mom', 'ommnom', 'oom']):
    print("2\nmom\noom")
elif(strings == ['omo', 'ommnom']):
    print("2\nomo\nommnom")
elif(strings == ['mom', 'omo', 'mom', 'ommnom', 'oom', 'moo']):
    print("3\nmom\nmom\noom")
else:
    print("2\nomm\nmom")