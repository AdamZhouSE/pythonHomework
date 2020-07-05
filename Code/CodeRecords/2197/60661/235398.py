t = int(input())
for i in range(t):
    num = int(input())
    record = []
    for i in range(num):
        record.append(i+1)
    pos = 0
    for j in range(num-1):
        del record[(pos+1)%len(record)]
        if pos<len(record):
            pos=(pos+1)%len(record)
        else:
            pos=0
    print(record[0])