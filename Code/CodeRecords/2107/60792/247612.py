def judge(n):
    i=0
    while 2**i<n:
        i=i+1
    if(2**i==n):
        return True
    else:
        return False
    

n=int(input())
if(judge(n)):
    print("True")
else:
    print("False")