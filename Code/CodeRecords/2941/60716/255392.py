n = int(input())
marklist = input()
dicts = {"A":4,"B":3,"C":2,"D":1,"E":0,"F":0}
index = 0
for i in range(n):
    index = index+dicts[marklist[i]]
i = double(index/n)
print(i)