m=int(input())
n=int(input())
M=[[0 for i in range(n)] for i in range(m)]
number=int(input())
for i in range(number):
    instru=input().split(",")
    j=0
    while j<m and j<int(instru[0]):
        k=0
        while k<n and k<int(instru[1]):
            M[j][k]+=1
            k+=1
        j+=1
maxNum=M[0][0]
times=0
i=0
while i<m:
    j=0
    while j<n:
        if M[i][j]==M[0][0]:
            times+=1
        j+=1
    i+=1
print(times)