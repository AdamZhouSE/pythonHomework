times=int(input())
for i in range(times):
    line1=input().split()
    line2=input().split()
    line1=[int(x) for x in line1]
    line2=[int(x) for x in line2]
    answer=[]
    for i in range(line1[0]-line1[1]+1):
        s=0
        for j in range(line1[1]):
            s+=line2[i+j]
        answer.append(s)
    answer.sort(reverse=True)
    print(answer[0])