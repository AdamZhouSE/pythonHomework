n=(int)(input())
instrctions=[]
meetings=[]
for i in range(n):
    instrctions.append(input().split(' '))
for i in instrctions:
    if(i[0]=='A'):
        j=0
        sum=0
        while(j<len(meetings)):
            if((meetings[j][0]>=(int)(i[1]) and meetings[j][0]<=(int)(i[2])) or(
                meetings[j][1]>=(int)(i[1]) and meetings[j][1]<=(int)(i[2])) or(
                meetings[j][0]<=(int)(i[1]) and meetings[j][1]>=(int)(i[2]))):
                del meetings[j]
                sum+=1
            else:
                j+=1
        print(sum)
        meetings.append([(int)(i[1]),(int)(i[2])])
    elif(i[0]=='B'):
        print(len(meetings))
