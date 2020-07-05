def sort(a):          
    m = len(a)-1
    while( m >= 0):
	    for n in range(m):
		    if(a[n] > a[n+1]):
			    temp = a[n+1]
			    a[n+1] = a[n]
			    a[n] = temp
	    m -=1
    return a

T = int(input())
x = 0
N,a =[],[]
while(x < T):
    N.append(input())
    a.append([int(i) for i in input().split()])
    x +=1
result = []
for item in a:
    result.append(sort(item));
for item in result:
    for i in range(len(item)):
        if(i != len(item)-1):
            print(item[i],end=' ')
        else:
            print(item[i])