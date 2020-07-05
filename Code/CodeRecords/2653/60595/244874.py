def Test():
    s=input().split()
    patients=int(s[0])
    cometime=int(s[1])
    count=0
    doctor=[]
    line=[]
    for i in range(0,100):
        if(i%10==0 and doctor):
            doctor.remove("Man")
        if(i%cometime==0 and patients!=0):
            line.append("Man")
            patients=patients-1
        if(not doctor):
            doctor.append("Man")
            line.remove(line[0])
        if(patients==0):
            if(not line):
                break
            count=count+1

    print(count)

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()