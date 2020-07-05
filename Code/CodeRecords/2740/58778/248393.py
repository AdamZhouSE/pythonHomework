s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    i=i[1:len(i)-1]
    h=i[0:2]
    m=i[3:5]
    time=int(h)*60+int(m)
    numlist.append(time)
di=[]
for i in range(len(numlist)-1):
    for j in range(i+1,len(numlist)):
        if(numlist[i]!=0 and numlist[j]!=0 and numlist[i]!=1440 and numlist[j]!=1440):
            di.append(abs(numlist[j]-numlist[i]))
        elif (numlist[i]==0 and numlist[j]!=0):
            if(numlist[j]>720):
                numlist[i]=1440
                di.append(abs(numlist[j]-numlist[i]))
        elif (numlist[i] != 0 and numlist[j] == 0):
            if (numlist[i] > 720):
                numlist[j] = 1440
                di.append(abs(numlist[j] - numlist[i]))
        elif (numlist[i] == 1400 and numlist[j] != 1400):
            if (numlist[j] < 720):
                numlist[i] = 0
                di.append(abs(numlist[j] - numlist[i]))
        elif (numlist[i] !=1440 and numlist[j] == 1400):
            if (numlist[j] < 720):
                numlist[j] = 0
                di.append(abs(numlist[j] - numlist[i]))
print(min(di))
#print(numlist)