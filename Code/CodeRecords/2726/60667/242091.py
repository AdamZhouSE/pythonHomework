tree = input()
new = tree.replace('null','None')
t = eval(new)
for i in range(len(t)-1):
    if t[i] is None and t[i+1] is None:
        print(int((i+1)/2))