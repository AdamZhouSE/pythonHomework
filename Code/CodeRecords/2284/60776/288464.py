a=int(input())
for k in range(0,a):
    max=0
    a=input()
    b = input().split(' ')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    for i in range(0,len(b)):
        for j in range(len(b)-1,i-1,-1):
            if b[j]>b[i]:
                if j-i>max:
                    max=j-i
                break
    print(max)