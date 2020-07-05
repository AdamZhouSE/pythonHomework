cus = [int(i) for i in input().split(',')]
gru = [int(i) for i in input().split(',')]
x = int(input())
out = 0
for i in range(len(gru)-x+1):
    temp = 0
    for j in range(len(gru)):
        if(i<=j and j<=i+x-1):
            temp+=cus[j]*1
        else:temp+=cus[j]*(1-gru[j])
    out = max(temp,out)
print(out)