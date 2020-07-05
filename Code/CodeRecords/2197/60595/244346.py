def Test():
    people=int(input())
    line=[]
    for i in range(1,people+1):
        line.append(i)
    i=0
    knife=1
    while(len(line)!=1):
        if(i==len(line)):
            i=0
        if(line[i]==knife):
            line.remove(next(i,line))
            knife=(line[i+1] if(i+1<len(line)) else line[0])
        else:
            i=i+1

    print(line[0])

def next(i,line):
    j=i+1
    if(j==len(line)):
        j=0
    return line[j]
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()