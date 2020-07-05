data=input().split("-")
year=int(data[0])
month=int(data[1])
day=int(data[2])
sum=0
month_arr=[31,28,31,30,31,30,31,31,30,31,30,31]
if year%4==0:
    month_arr[1]=29
for i in range(month-1):
    sum=sum+month_arr[i]
sum=sum+day
print(sum)
