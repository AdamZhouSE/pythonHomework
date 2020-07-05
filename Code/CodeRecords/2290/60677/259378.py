times=int(input())
def do():
    n=int(input())
    line=input().split()
    answer=[]
    for i in range(n-1):
        if line[i]>line[i+1]:
            answer.append(str(line[i+1]))
        else:
            answer.append(str(-1))
    answer.append(str(-1))
    return answer

for i in range(times):
    answer=do()
    for i in answer:
        print(i,end=" ")
    print()
