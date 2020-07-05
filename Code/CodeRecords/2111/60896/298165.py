a=eval(input())
count=0
n=1
while(True):
    num=n
    while (num % 2 == 0):
	    num /= 2
    while (num % 3 == 0):
	    num /= 3
    while (num % 5 == 0):
	    num /= 5
    if(num==1):
        count+=1
    if(count==a):
        print(n)
        break
    n+=1