def sort(a):          
    m = len(a)-1
    while( m >= 0):
	    for n in range(len(a)-1):
		    if(a[n] > a[n+1] ):
			    temp = a[n+1]
			    a[n+1] = a[n]
			    a[n] = temp
	    m -=1
    index = 1
    result = -1
    for i in range(len(a)):
        if(a[i] <= 0):
            index -=1
        elif(a[i] != i+index):
            
            result = i+index
            break
        elif( i == len(a)-1):
            result = a[i]+1
    return result



T = int(input())
x = 0
N,a =[],[]
while(x < T):
    N.append(int(input()))
    temp = [int(i) for i in input().split()]
    a.append(temp)
    x +=1
result = []
for item in a:
    result.append(sort(item));
for item in result:
    print(item)
