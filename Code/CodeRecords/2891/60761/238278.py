n=int(input(""))
pension=list(map(int,input("").split(" ")))
print(max(pension)*n-sum(pension))