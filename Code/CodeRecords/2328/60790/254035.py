import itertools
list1=input().split(",")
list1=list(map(int,list1))
ans=-1
for h1,h2,m1,m2 in itertools.permutations(list1):
    hour=10*h1+h2
    minitue=10*m1+m2
    time=60*hour+minitue
    if(0<=hour<24 and 0<=minitue<60 and time>ans):
        ans=time
if(ans>0):
    print("{:02}:{:02}".format(*divmod(ans, 60)))
else:
    print("")