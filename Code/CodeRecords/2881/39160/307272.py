n=int(input())
a=[f'{"D"*i:*^{n}}'for i in range(1,n,2)]
print(*a,'D'*n,*a[::-1],sep='\n')