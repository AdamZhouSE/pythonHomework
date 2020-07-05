n=int(input())
for i in range((n+1)//2):
    print("*"*((n-2*i-1)//2),"D"*(2*i+1),"*"*((n-2*i-1)//2),sep="")
for i in range((n-1)//2):
    print("*"*(i+1),"D"*(n-2*i-2),"*"*(i+1),sep="")