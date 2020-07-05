numOftests = int(input())
for i in range(numOftests):
    n = int(input())
    sum0 = 0
    for k in range(1,2*n,2):
        sum0+=((k+1)**2)//4
    print(sum0)