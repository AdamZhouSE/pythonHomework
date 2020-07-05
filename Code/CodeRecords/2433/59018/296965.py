def isok(list):

    for i in range(len(list)-1):
        if(list[i][1]>=list[i+1][0]):
            return False
    return True
list=[]
string=input()
string=string[2:-2]

string=string.split("],[")

for i in range(len(string)):
    m=string[i].split(",")

    a=int(m[0])
    b=int(m[1])
    list.append([a,b])
while(True):
    '''print(list)'''
    length = len(list)
    time=0
    for i in range(len(list)):
        if(i>=length):
            break;
        intime=0
        for j in range(i+1,len(list)):
            if(j>=length):
                break;
            if(i==j): continue
            else:
                if((list[i][0]<=list[j][1])&(list[i][1]>=list[j][0])):
                    s=[list[i][0],list[j][1]]
                    del(list[i])
                    del(list[j-1])
                    list.append(s)
                    length-=1
                intime+=1
        time+=1
    for i in range(length):
        for m in range(length-1):
            if(list[m][0]>list[m+1][0]):
                mid=list[m+1]
                list[m+1]=list[m]
                list[m]=mid
    if( isok(list)):
        break

print(list)