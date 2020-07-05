t = int(input())
for i in range(t):
    num = int(input())
    record = []
    for i in range(num):
        record.append(i+1)
    p = 1
    for j in range(num-1):
        pos = record.index(p)
        del record[(pos+1)%len(record)]
        if pos<len(record):
            pos=(pos+1)%len(record)
        else:
            pos=0
        p=record[pos]
    print(record[0])