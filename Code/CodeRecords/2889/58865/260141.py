n=int(input().strip())
arr=input().split(' ')
arr=[int(i) for i in arr]
print('{0:.6f}'.format(sum(arr)/n))