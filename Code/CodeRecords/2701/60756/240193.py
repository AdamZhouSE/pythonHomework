firstLine=input()
stepList=firstLine[1:-1].split("],[")
stepList[0]=stepList[0][1:]
stepList[-1]=stepList[-1][:-1]
xStep=[]
oStep=[]
for i in range(len(stepList)):
    if i%2==0:
        xStep.append(''.join(stepList[i].split(",")))
    else:
        oStep.append(''.join(stepList[i].split(",")))
winner="Pending"
if (("00" in xStep)&("11" in xStep)&("22" in xStep))|(("00" in xStep)&("01" in xStep)&("02" in xStep))|(("10" in xStep)&("11" in xStep)&("12" in xStep))|(("20" in xStep)&("21" in xStep)&("22" in xStep))|(("00" in xStep)&("10" in xStep)&("20" in xStep))|(("01" in xStep)&("11" in xStep)&("21" in xStep))|(("02" in xStep)&("12" in xStep)&("22" in xStep))|(("02" in xStep)&("11" in xStep)&("20" in xStep)):
    winner="A"
elif (("00" in oStep)&("11" in oStep)&("22" in oStep))|(("00" in oStep)&("01" in oStep)&("02" in oStep))|(("10" in oStep)&("11" in oStep)&("12" in oStep))|(("20" in oStep)&("21" in oStep)&("22" in oStep))|(("00" in oStep)&("10" in oStep)&("20" in oStep))|(("01" in oStep)&("11" in oStep)&("21" in oStep))|(("02" in oStep)&("12" in oStep)&("22" in oStep))|(("02" in oStep)&("11" in oStep)&("20" in oStep)):
    winner="B"
elif len(stepList)==9:
    winner="Draw"
print(winner)