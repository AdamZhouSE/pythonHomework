cases=int(input())
for i in range(cases):
    a_b=input().split()
    a,b=int(a_b[0]),int(a_b[1])
    least_sum=int(b*(b+1)/2)
    if a<least_sum:
        print('0')
    else:
        print('1')