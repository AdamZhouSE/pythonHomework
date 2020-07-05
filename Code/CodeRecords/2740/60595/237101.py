def Test():
    s=input()
    s=s.replace("["," ")
    s=s.replace("]"," ")
    s=s.replace("\""," ")
    s=s.replace(" ","")
    s=s.strip()
    line=s.split(",")
    time=[]
    small=24*60
    for x in line:
        y=x.split(":")
        time.append(int(y[0])*60+int(y[1]))
    for i in range(0,len(time)):
        for j in range(i,len(time)):
            if(i!=j):
                temp1=abs(time[i]-time[j])
                temp2=24*60-abs(time[i]-time[j])
                if(temp1<small):
                    small=temp1
                if(temp2<small):
                    small=temp2
    print(small)

if __name__ == "__main__":
    Test()