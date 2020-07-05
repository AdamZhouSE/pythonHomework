A = list(map(int,input()[1:-1].split(',')))
A = sorted(A)
last = A[0]
count = 1
record = []
for i in range(1,len(A)):
    if(A[i] == last + 1):
        last = last + 1
        count = count + 1
    else:
        record.append(count)
        count = 1
        last = A[i]
print(max(record))