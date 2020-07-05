S=input()+' ';n=len(S)-1;l=r=i=0
re = []
while i<n:
	i+=1;c=S[l+(i-l)%(r-l+1)]
	if S[i]>c:r=i
	elif S[i]<c:
		while r<i:re.append(r+1),;l,r=r+1,r+r-l+1
		i=r=l
print(' '.join('%s' %id for id in re))

