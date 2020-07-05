strLst = input()[2:-2].split('","')
max = 0
for i in range(0,len(strLst) - 1):
    s1 = list(strLst[i])
    for j in range(i + 1,len(strLst)):
        s2 = list(strLst[j])
        temp = [ch for ch in s1 if ch in s2]
        if(len(temp) == 0):
            if(len(s1) * len(s2) > max):
                max = len(s1) * len(s2)
print(max)