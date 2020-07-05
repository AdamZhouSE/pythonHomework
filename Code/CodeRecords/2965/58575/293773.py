KM=list(map(int,input().split(" ")))
K=KM[0]
M=KM[1]
S=input()
number=int(input())

i=0
while i<number:
    temp=list(map(int,input().split(" ")))
    A=temp[0]
    B=temp[1]
    C=temp[2]

    Copy=S[A:B]
    S=S[0:C]+Copy+S[C:]
    if len(S)>M:
        S=S[0:M]
    i=i+1
print(S[0:K],end="")