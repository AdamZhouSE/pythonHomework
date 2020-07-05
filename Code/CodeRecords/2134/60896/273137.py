buckets=eval(input())
die_time=eval(input())
total_time=eval(input())
num=0
while(total_time/die_time+1)**num<buckets:
    num+=1
print(num)