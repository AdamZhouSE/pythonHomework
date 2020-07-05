null = "a"
m = input()
n = input()
root1 = eval(m)
root2 = eval(n)
ans = root1 + root2
if "a" in ans:
    ans.remove("a")
print(list(sorted(ans)))
