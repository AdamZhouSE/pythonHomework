times=int(input())
for i in range(times):
    line1=input().split()
    line2=input().split()
    line1=[int(x) for x in line1]
    line2=[int(x) for x in line2]
    answer=0
    if (line2[0]>=line1[0] and line2[0]<=line1[2]) or (line2[2]>=line1[0] and line2[2]<=line1[2]) or (line2[2]>=line1[0] and line2[0]<=line1[0]) or (line2[2]>=line1[2] and line2[0]<=line1[2]):
        if(line2[1]>=line1[3] and line2[1]<=line1[1]) or (line2[3]>=line1[3] and line2[3]<=line1[1]) or (line2[1]>=line1[1] and line2[3]<=line1[1]) or (line2[1]>=line1[3] and line2[3]<=line1[3]):
            answer=1
    if line2[0]==line1[2] and line2[1]==line1[3]:
        answer=0
    if line1[0]==line2[2] and line1[1]==line2[3]:
        answer=0
    print(answer)
