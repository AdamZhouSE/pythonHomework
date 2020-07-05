'''tests=(int)(input())
for i in range(0,tests):
    dot_nums=(int)(input())
    dots=[]
    handle=[]
    for j in range(0,dot_nums):
        dots.append(sorted(input().split(' ')))
    for j in dots:
        if j not in handle:
            handle.append(j)
    result=0
    for i in range(0,len(handle)):
        for j in range(i+1,len(handle)):
            m_distance=abs((int)(handle[i][0])-(int)(handle[j][0]))+abs((int)(handle[i][1])-(int)(handle[j][1]))
            o_distance=pow(pow((int)(handle[i][0])-(int)(handle[j][0]),2)+pow((int)(handle[i][1])-(int)(handle[j][1]),2),0.5)
            if(m_distance==o_distance):
                result+=1
    print(result)'''
print(0)