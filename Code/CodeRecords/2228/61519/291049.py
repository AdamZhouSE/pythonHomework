n=int(input())
if n<0:
    n=-n
i=0
num=0
while True:
    if num>=n and (num-n)%2==0:
        print(i)
        break
    i+=1
    num=num+i