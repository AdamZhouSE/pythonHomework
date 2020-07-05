s = input()
listOfnums = list(map(int,s[s.index("[")+1:s.index("]")].split(",")))
k = int(s[s.find("k")+4])
t = int(s[s.find("t")+4])
result = False
for i in range(0,len(listOfnums)-k):
    for j in range(i+1,min(len(listOfnums),i+k+1)):
        if abs(listOfnums[i]-listOfnums[j])<=t:
            result = True
            break
if result:print("true")
else :print("false")