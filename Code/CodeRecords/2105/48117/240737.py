s = input().split(', ')
xA = int(s[0])
yA = int(s[1])
xB = int(s[2])
yB = int(s[3])
xC = int(s[4])
yC = int(s[5])
xD = int(s[6])
yD = int(s[7])

Sab = (xB - xA) * (yB - yA)
Scd = (xD - xC) * (yD - yC)

if  (xA > xC and yA > yC) or (xA < xC and yA > yC):
    s1a = abs(xA - xC)
    s1b = abs(yA - yC)
    s2a = abs(xD - xB)
    s2b = abs(yB - yD)
else:
    s1a = abs(xA - xC)
    s1b = abs(yB - yD)
    s2a = abs(xD - xB)
    s2b = abs(yA - yC)

S1 = s1a * s1b
S2 = s2a * s2b
S = max(abs(xA - xD), abs(xB - xC)) * max(abs(yA - yD), abs(yB - yC))




if xA > xD or xC > xB:
    print(0)
elif yA > yD or yC > yB:
    print(0)
else:
    print(S - S1 - S2)