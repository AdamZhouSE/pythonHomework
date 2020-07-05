A = list(map(int,input()[1:-1].split(',')))
flag = True
high = A[0]
low = 0
cut = 0
while(flag):
    cut = cut + 1
    while(low <= high):
        if(A[low] > high):
            high = A[low]
        if(high == len(A) - 1):
            flag = False
            break
        low = low + 1
    if(flag):
        high = A[high + 1]
    else:
        break
print(cut)