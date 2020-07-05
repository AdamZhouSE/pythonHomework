a=int(input())
b=int(input())
c=int(input())

minPos=min(a,b,c)
maxPos=max(a,b,c)

minStep=1
if maxPos-minPos==2:
	minStep=0
print("[{}, {}]".format(minStep,maxPos-minPos-2))