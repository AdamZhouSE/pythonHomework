while(True):
    n=(int)(input())
    if(n==0):
        break
    pattern=[]
    for i in range(n):
        pattern.append(input())
    txt=input()
    t_length=len(txt)
    record_frequency=[]
    start=0
    for i in pattern:
        frequency=0
        length=len(i)
        for j in range(t_length+1-length):
            if(txt[j]==i[0]):
                if(txt[j:j+length]==i):
                    frequency+=1
        record_frequency.append(frequency)
    max_frequency=max(record_frequency)
    print(max_frequency)
    for i in range(len(record_frequency)):
         if(record_frequency[i]==max_frequency):
             print(pattern[i])