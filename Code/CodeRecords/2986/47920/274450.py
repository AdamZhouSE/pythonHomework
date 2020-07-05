#stra: sda_sdah
#strb 123124sd
#_aaddhss
#112234ds

stra = input()
strb = input()

la = list(stra)
la.sort()
stra1 = "".join(la)

lb = list(strb)
lb.sort()
strb1 = "".join(lb)
count = 0
chaj = abs(len(stra)-len(strb))
for i in range(len(stra1)):
    for j in range(len(strb1)):
        if(stra[i] == strb[j]):
            count = count +1
            break;
print(chaj + len(stra1)-count)

            
