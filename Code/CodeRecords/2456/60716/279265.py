lists = list(eval(input()))
ans = list()
while lists>0:
    index = lists.pop(0)
    temp = [ 1 if i<index else 0 for i in lists]
    ans.append(temp.count(1))
print(ans)