n = int(input())
count = 0
i =0
while(count<n):
    i += 1
    count+=i


if count==n:
    result =i
elif (count-n)%2==0:
    result =i
elif (count-n)%2==1 and i%2==0:
    result= i+1
else:
    result = i+2

print(result)
