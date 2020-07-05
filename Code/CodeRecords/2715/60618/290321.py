n=eval(input())
a = [i[0] for i in n]
b = [i[1] for i in n]
print(len(n)-min(len(set(a)),len(set(b))))