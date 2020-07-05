T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    for i in range(0,N-1):
        if source[i]==source[i+1]:
            source[i]=str(int(source[i])*2)
            source[i+1]="0"
            i += 1
    result = ""
    for i in source:
        if i != '0':
            result = result + i + " "
    for j in range(len(result)//2, N):
        result = result + "0 "
    print(result.rstrip(' '))
    