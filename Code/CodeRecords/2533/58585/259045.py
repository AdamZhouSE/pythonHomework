A=input()
B=A[1:-1].split(',')
B=list(map(int,B))
print(sorted(B)[::-1])