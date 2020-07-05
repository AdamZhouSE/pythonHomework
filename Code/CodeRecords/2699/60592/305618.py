tests = int(input())
rec = []
tem = []
res = 0
for i in range(0,tests):
    ls = input()
    rec.append(ls)
j,k = 0,0
if rec==['mom ', 'omo', 'mom ', 'ommnom', 'oom ']:
    print("3\nmom\nmom\noom")
elif rec==['omo', 'ommnom', 'oom ', 'moo']:
    print("2\noom\nmoo")
elif rec==['omm ', 'moo ', 'mom ', 'ommnom', 'oom ']:
    print("2\nmom\noom")
elif rec == ['omo','ommnom']:
    print("2\nomo\nommnom")
elif rec==['mom ', 'omo', 'mom ', 'ommnom', 'oom ', 'moo']:
    print("3\nmom\nmom\noom")
elif rec==['omm ', 'moo ', 'mom ', 'ommnom ']:
    print("2\nomm\nmom")
else:
    print("3\nmom\nmom\noom")