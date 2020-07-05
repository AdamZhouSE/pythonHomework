str1=list(map(int,input().split(",")))
str2=list(map(int,input().split(",")))
maxNum=0
i=0
while i<len(str1):
    j=0
    while j<len(str1):
          maxNum=max(maxNum,abs(str1[i]-str1[j])+abs(str2[i]-str2[j])+abs(i-j))
          j=j+1
    i=i+1
print(maxNum)