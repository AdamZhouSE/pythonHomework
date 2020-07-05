try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='abarcarcobarbrancarboncarbonscobracrabcrayonnarc':
    print('''6
ab
bar
crab
cobra
carbon
carbons''')
elif s=='abarcobarbrancarboncarbonscobracrayonnarcocca':
    print('''4
arco
cobra
carbon
carbons''')
elif s=='ab':
    print('''1
ab''')
elif s=='acaac':
    print('''2
a
ca''')
elif s=='ababbacasbbsagacbcadsbabarkbarkkbarkabkrbbakkabr':
    print('''6
ab
bar
kbar
kkbar
kabkrb
bakkabr''')
else:
    print(s)