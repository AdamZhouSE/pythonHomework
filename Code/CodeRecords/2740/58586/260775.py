times=eval(input())
mix=1440
def calculate(s1,s2):
    [t1,m1]=list(map(int,s1.split(":")))
    [t2,m2]=list(map(int,s2.split(":")))
    T1=t1*60+m1
    T2=t2*60+m2
    temp=abs(T1-T2)
    return min(temp,1440-temp)
for i in range(len(times)-1):
    for j in range(i+1,len(times)):
        mix=min(mix,calculate(times[i],times[j]))
print(mix)