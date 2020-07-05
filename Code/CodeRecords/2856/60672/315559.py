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

n=int(input())
trees=[[0,0] for i in range(n)]
for i in range(n):
    string=nums(input())
    trees[i]=string
answer=2
for i in range(1,len(trees)-1):
    left=trees[i-1][0]
    right=trees[i+1][0]
    if trees[i][1]<trees[i][0]-left:
        answer+=1
    elif trees[i][1]<right-trees[i][0]:
        trees[i][0]+=trees[i][1]
        answer+=1
print(answer)