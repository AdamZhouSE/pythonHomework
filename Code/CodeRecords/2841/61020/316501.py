import math
def create(a,n,k):
	t = [0]*n+a
	for i in range(n-1,0,-1):
	    z = int(math.log(i,2))
	    if(k%2==0):
	    	if(z%2):
	    		t[i] = t[2*i]|t[2*i+1]
	    	else:
	    		t[i] = t[2*i]^t[2*i+1]
	    else:
	    	if(z%2):
	    		t[i] = t[2*i]^t[2*i+1]
	    	else:
	    		t[i] = t[2*i]|t[2*i+1]
	return t

def update(idx,value,t,n,k):
	idx = idx+n
	t[idx] = value

	while(idx>1):
		idx = idx>>1
		z = int(math.log(idx,2))
		if(not(k&1)):
		    if(z%2):
		        t[idx] = t[2*idx]|t[2*idx+1]
		    else:
		    	t[idx] = t[2*idx]^t[2*idx+1]
		else:
			if(z%2):
				t[idx] = t[2*idx]^t[2*idx+1]
			else:
				t[idx] = t[2*idx]|t[2*idx+1]
	return t
import sys
n,m = map(int,sys.stdin.readline().strip().split())
k = n
l = list(map(int,sys.stdin.readline().strip().split()))
t = create(l,2**n,k)
#print(t)
for _ in range(m):
    idx,value = map(int,sys.stdin.readline().strip().split())
    t = update(idx-1,value,t,2**n,k)
    print(t[1])