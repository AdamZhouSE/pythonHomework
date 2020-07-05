#even can be balanced, odd can't

time=int(input())
result=[]

while time>0:
    seq=input()                 #}{{}}{{{
    if len(seq)%2==0:
        bracket=[i for i in seq]

        fro_table=[]
        for i in range(0,len(seq)):
            if bracket[i]=='{':
                fro_table.append(i)
            else:
                if len(fro_table)>0:
                    bracket[i]='none'
                    bracket[fro_table[-1]]='none'
                    fro_table.remove(fro_table[-1])

        adjust=[]
        for token in bracket:
            if token!='none':
                adjust.append(token)
        if len(adjust)%2!=0:
            result.append(-1)
        else:
            count=0
            for j in range(0,len(adjust),2):
                if adjust[j]==adjust[j+1]:
                    count=count+1
                else:
                    count=count+2
            result.append(count)

    else:
        result.append(-1)
    time=time-1
for res in result:
    print(res)

