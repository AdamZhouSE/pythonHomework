def getValue(string):
    length = 3
    add = 0
    if len(string)<length:
        length = len(string)
    for j in range(3):
        temp = words.find(len(string)-j-1)
        add += temp*((26+len(string))**(2-j))

n,p = map(int,input().split())
strs = input().split()
words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lists = list()
for i in range(n):
    index = getValue(strs[i])
    if index in lists:
        index=collision(index)
    lists.append(index)
a = [str(i) for i in lists]
answer = ' '.join(a)
print(answer)