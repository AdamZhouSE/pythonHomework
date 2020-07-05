A = list(map(int,input()[1:-1].split(',')))
B = sorted(A)
low = 0
high = len(A) - 1
while(high >= low):
    if(B[low] == A[low]):
        low = low + 1
    else:
        break
while(high >= low):
    if(B[high] == A[high]):
        high = high - 1
    else:
        break
print(high - low + 1)