times=int(input())
for i in range(times):
    line1=input().split()
    line2=input().split()
    line1=[int(x) for x in line1]
    line2=[int(x) for x in line2]
    line2.sort(reverse=True)
    answer=0
    for i in range(line1[1]):
        answer+=line2[i]
    print(answer)