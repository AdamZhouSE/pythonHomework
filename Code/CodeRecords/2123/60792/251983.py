def judge(n):
    i=0
    while i*i<n:
        i=i+1
    if(i*i==n):
        return True
    else:
        return False

    
n=int(input())
print(judge(n))