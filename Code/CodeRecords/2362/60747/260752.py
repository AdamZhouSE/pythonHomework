N=int(input())
a=0
if N <= 2:
    print(N)

elif N <= 4:
    print(N + 3)
    a=-1
if (N - 4) % 4 == 0and a!=-1:

    print(N + 1)

elif (N - 4) % 4 <= 2 and a!=-1:

    print(N + 2)

else:
    print(N - 1)
