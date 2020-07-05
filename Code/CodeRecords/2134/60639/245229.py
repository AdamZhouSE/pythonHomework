n=int(input())
minitestoDie=int(input())
minitestoTest=int(input())
num=minitestoTest/minitestoDie+1
pro=1
pig=0
while pro<n:
    pro=pro*num
    pig+=1
print(pig)