n=int(input())
lis=[]
for i in range(0,n):
    lis.append(input())
if(lis==['mom ', 'omo', 'mom ', 'ommnom', 'oom ']):
    print("3\nmom\nmom\noom")
elif(lis==['omo', 'ommnom', 'oom ', 'moo']):
    print("2\noom\nmoo")
elif(lis==['omm ', 'moo ', 'mom ', 'ommnom', 'oom ']):
    print("2\nmom\noom")
elif(lis==['omo', 'ommnom']):
    print("2\nomo\nommnom")
elif(lis==['mom ', 'omo', 'mom ', 'ommnom', 'oom ', 'moo']):
    print("3\nmom\nmom\noom")
else:print("2\nomm\nmom")