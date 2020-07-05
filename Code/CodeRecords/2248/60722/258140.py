N=int(input())
A=int(input())
B=int(input())
i=0
num=0
while i!=N:
    num+=1
    if num%A==0 or num%B==0:
        i+=1
print(num)