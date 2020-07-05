n=int(input())
a=int(input())
b=int(input())
number=0
count=0
while count<n:
    number+=1
    if number%a==0 or number%b==0:
        count+=1

print(number%(pow(10,9)+7))