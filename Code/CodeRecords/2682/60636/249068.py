t=int(input())
for i in range(t):
    source=input().split()
    sources=[]
    for j in source:
        sources.append(int(j))
    bin_number=list(bin(sources[0]))
    for j in range(sources[1],sources[2]+1):
        if(bin_number[j+2]=="0"):
            bin_number[j+2]="1"
        else:
            bin_number[j+2]="0"
    res=""
    for a in bin_number:
        res=res+a
    print(int(res,2))
    