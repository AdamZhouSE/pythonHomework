v = int(input())
lis = list(map(int,input().split()))
proverka = 0
if v == 0 or v < min(lis):
    print(-1)
    exit(0)

best = 1000000000
for i in range(len(lis)-1,-1,-1):
    if lis[i] < best:
        best = lis[i]
        ind = i + 1
        
st = []
while (True):
    if ((v - best) < 0):
        break
    else:
        st.append(ind)
    v -= best


for i in range(len(st)):
    st[i] = int(st[i])
    
for i in range(len(st)):
    
    if v == 0:
	    break
    #print(v)
    v += best
    
    for s in range(len(lis)):
        if v > lis[s] :
            proverka += 1
    if proverka == 0:
        break
    #print(proverka,v)
    proverka = 0    
    for j in range(len(lis)-1,-1,-1):
	    if (v >= lis[j]) and (j + 1 >= st[i]):
		    st[i] = j + 1
			
		    v -= lis[j]
	
		


print("".join(map(str,st))) 