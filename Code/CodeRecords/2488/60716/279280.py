lists = list(eval(input()))
lists.sort()
ans = [lists[i] if i%2==0 else lists[(len(lists)+1+i)//2] for i in range(len(lists))]
print(ans)