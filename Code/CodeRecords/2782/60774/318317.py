n = int(input())
f = int(input())
day = [f]
for i in range(1,n):
    pro = int(input())
    min = abs(pro - day[0])
    for k in range(1,i):
        if(abs(pro - day[k]) < min):
            min = abs(pro - day[k])
    f = f + min
print(min)