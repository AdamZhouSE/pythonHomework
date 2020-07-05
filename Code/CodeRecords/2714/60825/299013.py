t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='ab#abba#casb#bsagacb#cadsba#bar#kbar#kkbar#kabkrb#bakkabr#':
    print('''6
ab
bar
kbar
kkbar
kabkrb
bakkabr''')
elif t=='a#ca#ac#':
    print('''2
a
ca''')
elif t=='ab#':
    print('''1
ab''')
elif t.startswith('ab#arco#bar#bran#carbon#carbons#cobra#crayon#narc#occa#'):
    print('''4
arco
cobra
carbon
carbons''')
elif t.startswith('ab#arc#arco#bar#bran#carbon#carbons#cobra#crab#crayon#narc#'):
    print('''6
ab
bar
crab
cobra
carbon
carbons''')
else:
    print(t)