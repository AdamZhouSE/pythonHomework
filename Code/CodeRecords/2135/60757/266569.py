arr=sorted(list(eval(input())))
arr_cal=arr[:]
n=len(arr)
middle=0
if n%2==0:
    for i in range(n/2-1):
        del arr_cal[arr_cal.index(max(arr_cal))]
        del arr_cal[arr_cal.index(min(arr_cal))]
    middle=arr_cal[0]
else:
    for i in range(n//2):
        del arr_cal[arr_cal.index(max(arr_cal))]
        del arr_cal[arr_cal.index(min(arr_cal))]
    middle=arr_cal[0]
count=0
for i in range(n):
    count=count+abs(middle-arr[i])
print(count)