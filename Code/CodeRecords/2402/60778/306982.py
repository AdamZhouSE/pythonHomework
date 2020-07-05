lines=int(input())
answer=[]
for i in range(lines):
    booking=list(map(int,input().split(',')))
    for j in range(booking[0],booking[1]+1):
        while(len(answer)<j):
              answer+=[0];
        answer[j-1]+=booking[2];
n=int(input())
print(answer)