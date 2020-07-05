import sys
tests=(int)(input())
for i in range(tests):
    meetings=(int)(input())
    s=list(map(int,input().strip().split(' ')))
    f=list(map(int,input().strip().split(' ')))
    end=min(f)
    start=s[f.index(end)]
    record=[s.index(start)+1]
    while(True):
        judge=False
        record_end =sys.maxsize
        for j in range(meetings):
            if(s[j]>end and f[j]<record_end):
                record_end=f[j]
                judge=True
        if(judge):
            end=record_end
            start=s[f.index(end)]
            record.append(s.index(start)+1)
        else:
            break
    for k in range(len(record)):
        if(k!=len(record)-1):
            print(record[k],end=' ')
        else:
            print(record[k],'')