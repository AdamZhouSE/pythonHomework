N=int(input())

i=1
s=""
while True:
    s=s+str(i)
    if len(s)>=N:
        print(s[N-1])
        break
    i=i+1

