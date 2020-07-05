def judge(n):
    i=0
    while 3**i<n:
        i=i+1
    if(3**i==n):
        return True
    else:
        return False
    

n=int(input())
if(judge(n)):
    print("True")
else:
    print("False")