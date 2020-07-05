n=int(input());
ans=[];
for i in range(n):
    N=int(input());
    height =[int(x) for x in input().split()];
    MAX = max(height);
    MAXindex = 0;
    area=0;
    for i in range(N):
        if(height[i]==MAX):
            MAXindex = i;
    leftMax=0;
    for i in range(MAXindex):
        if(height[i]<leftMax):
            area+=(leftMax-height[i]);
        else:
            leftMax = height[i];

    rightMax=0;
    for i in range(len(height)-1,MAXindex,-1):
        if(height[i]<rightMax):
            area+=(rightMax-height[i]);
        else:
            rightMax=height[i];
    ans.append(area);


for i in range(0,n-1):
    print(ans[i]);

print(ans[n-1]);
