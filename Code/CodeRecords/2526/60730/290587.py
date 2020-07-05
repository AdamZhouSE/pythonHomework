null = -10000
m = input()
n = input()
root1 = eval(m)
root2 = eval(n)
ans = root1+root2
ans.remove(-10000)
print(list(sorted(ans)))