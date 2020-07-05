case=(int)(input())
for i in range(case):
    mes=input().split(' ')
    length=(int)(mes[0])
    s=input().split(' ')
    t=input().split(' ')
    record=[[-1]*2 for _ in range(0,3)]
    slice=0
    result='YES'
    for j in range(0,length):
        if(s[j]!=-1):
            for k in range(0,length):
                if(t[k]!=-1 and t[k]==s[j]):
                    if(slice<3):
                        record[slice][0]=k+1
                        t[k]=-1
                        s[j]=-1
                        temp1=k
                        temp2=j
                        while(temp1+1<length and temp2+1<length and t[temp1+1]!=-1 and t[temp1+1]==s[temp2+1]):
                            temp1+=1
                            temp2+=1
                            t[temp1]=-1
                            s[temp2]=-1

                        record[slice][1]=temp1+1
                        slice+=1
                    else:
                        result='NO'
                        break
            if(result=='NO'):
                break
    for i in s:
        if(i!=-1):
            result='NO'         
    print(result)
    if (result == 'NO'):
        continue
    if(slice!=3):
        split_slice=slice-1
        while(record[split_slice][1]-record[split_slice][0]<1):
            split_slice-=1
        temp=list.copy(record[split_slice+1:])
        record=record[:split_slice+1]+[[-1]*2 for i in range(2-slice)]+temp
        for i in range(0,3):
            if(record[i][0]==-1):
                record[i][0]=record[split_slice][0]+1
                record[i][1]=record[split_slice][1]
                record[split_slice][1]=record[split_slice][0]
    for i in record:
        for j in range(2):
            if (j < 1):
                print(i[j],end=' ')
            else:
                print(i[j])
