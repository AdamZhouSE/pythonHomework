times=int(input())
def do():
    n=int(input())
    line=input().split()
    answer=[]
    for i in range(n-1):
        if line[i]>line[i+1]:
            answer.append(line[i+1])
        else:
            answer.append(-1)
        answer.append(-1)
    return answer

for i in range(times):
    print(" ".join(do()))
