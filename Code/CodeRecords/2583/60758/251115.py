n=int(input())
a=int(input())
b=int(input())
c=int(input())
num=1
out=[]
while True:
    if(num%a==0 or num%b==0 or num%c==0):
        out.append(num)
    if(len(out)==n):
        print(out[-1])
        break
    num+=1