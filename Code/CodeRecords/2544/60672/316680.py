def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
def cross(line1,line2):
    if line1[0]>line1[2]:
        line1[0],line1[2]=line1[2],line1[0]
        line1[1],line1[3]=line1[3],line1[1]
    if line2[0]>line2[2]:
        line2[0],line2[2]=line2[2],line2[0]
        line2[1],line2[3]=line2[3],line2[1]
    if (line1[3]-line2[3])*(line1[1]-line2[1])<=0:
        if line1[2]>=(-line2[0]+line2[2])/2+line2[0] or line1[3]>=(line2[3]-line2[1])/2+line2[1]:
            return 1
        elif line1[0]<=(-line2[0]+line2[2])/2+line2[0] or line1[1]<=(line2[3]-line2[1])/2+line2[1]:
            return 1
        else:
            return 0
    else:
        return 0
n=int(input())
for i in range(n):
    answer=0
    line1=nums(input())
    line2=nums(input())
    answer=cross(line1,line2)
    print(answer)