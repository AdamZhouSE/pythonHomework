def times_table():
    table=eval(input())
    mins_table=[]
    for time in table:
        mins=0
        mins+=int(time[0])*600
        mins+=int(time[1])*60
        mins+=int(time[3])*10
        mins+=int(time[4])
        mins_table.append(mins)
    result_set=[]
    for i in range(0,len(mins_table)-1):
        for j in range(i+1,len(mins_table)):
            if mins_table[i]==0:
                temp=min(abs(1440-mins_table[j]),abs(0-mins_table[j]))
            elif mins_table[j]==0:
                temp=min(abs(mins_table[i]-1440),abs(mins_table[i]-0))
            else:
                temp=abs(mins_table[i]-mins_table[j])
            result_set.append(temp)

    print(min(result_set),end="")

if __name__=='__main__':
    times_table()