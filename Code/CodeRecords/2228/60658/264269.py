target = abs(int(input()))
p,i=0,0
while p<target or (p+target)%2!=0:
    i+=1
    p+=i
print(i)