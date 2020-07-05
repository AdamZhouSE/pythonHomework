nums=int(input());
years=input().split(" ");
years=list(int(x) for x in years);
nowandtarget=input().split(" ");
now=int(nowandtarget[0]);
target=int(nowandtarget[1]);
result=0;
for i in range(now-1,target-1):
    result=result+years[i];
print(result)