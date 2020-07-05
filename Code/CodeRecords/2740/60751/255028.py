def calculate(str):
    str_=str.split(":")
    str_[0]=str_[0][1:3]
    str_[1] = str_[1][0:2]
    time_=int(str_[0])*60+int(str_[1])
    return time_

def sub(a,b):
    if a>b:
        a,b=b,a
    k=b-a
    m=a+24*60-b
    return min(k,m)
list=input().split(",")
list[0]=list[0][1:len(list[0])]
list[-1]=list[-1][1:len(list[-1])]
time=[]
for i in list:
    time.append(calculate(i))
min_=12*60
for i in range(len(time)):
    for j in range(i+1,len(time)):
        if sub(time[i],time[j])<min_:
            min_=sub(time[i],time[j])
print(min_)