strings=[]
try:
    while(True):
        s=input()
        strings.append([])
        while(s!="9"):
            strings[-1].append(s)
            s=input()
except:
    for group in strings:
        k=0
        for i in range(len(group)):
            for j in range(i+1,len(group)):
                if group[i].startswith(group[j]) or group[j].startswith(group[i]):
                    k=1
                    break
            if k==1:
                break
        if(k==1):
            print("Set "+str(strings.index(group)+1)+" is not immediately decodable")
        else:
            print("Set "+str(strings.index(group)+1)+" is immediately decodable")     
    