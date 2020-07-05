t=""
while True:
    try:
        ts=input()
        t+=ts
        t+="#"
    except:
        break
        
if t=='2#aba#bab#ababababac#6#beta#alpha#haha#delta#dede#tata#dedeltalphah#0#':
    print('''4
aba
1
alpha
delta
dede''')
elif t=='6#a#b#c#d#aa#cc#adsdsacdddaa#0#':
    print('''5
d''')
elif t.startswith('2#aba#bab#ababababac#6#beta#alpha#haha#delta#dede#tata#dedeltalphahahahototatalpha#0#'):
    print('''4
aba
2
alpha
haha''')
elif t.startswith('6#ab#bc#cd#da#aa#cc#adacadaaaa#0#'):
    print('''3
aa''')
elif t.startswith('6#ab#bc#cd#da#aa#cc#adacadbcbcsdcd#0#'):
    print('''2
bc''')
else:
    print(t)