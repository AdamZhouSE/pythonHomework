n=eval(input())
arr=[str(i+1) for i in range(n)]
string=''.join(arr)
print(string[n-1])