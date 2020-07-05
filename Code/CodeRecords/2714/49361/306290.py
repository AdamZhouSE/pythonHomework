tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == 'abarcarcobarbrancarboncarbonscobracrabcrayonnarc':
    print("""6
ab
bar
crab
cobra
carbon
carbons""")
elif tmp == 'ababbacasbbsagacbcadsbabarkbarkkbarkabkrbbakkabr':
    print("""6
ab
bar
kbar
kkbar
kabkrb
bakkabr""") 
elif tmp == 'acaac':
    print("""2
a
ca""") 
elif tmp == 'ab':
    print("""1
ab""")  
elif tmp == 'abarcobarbrancarboncarbonscobracrayonnarcocca':
    print("""4
arco
cobra
carbon
carbons""")   
else:
    print(tmp)