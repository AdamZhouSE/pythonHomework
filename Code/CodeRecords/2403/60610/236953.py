candies=input();
num_people=input();
ans=[];
for i in range (0,num_people):
    ans.append(0);
while candies!=0:
    j=0;
    while True:
        for i in range(0,num_people):
            if candies>=i+num_people*j:
                ans[i]=i+1+num_people*j+ans[i];
                candies=candies-i-num_people*j-1;
            else:
                ans[i]=ans[i]+candies;
                candies=0;
                break;
        if(candies==0):
            break;
        j=j+1;
        
print(ans);