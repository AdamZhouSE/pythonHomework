n = list(map(int,list(input())))
addn = sum(n)
miln = 1
for i in range(0,len(n)):
    miln *= n[i]
print(miln-addn)