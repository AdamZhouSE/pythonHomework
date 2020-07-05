num = int(input())
classes = eval(input())
dic = {}
for i in range(num):
    dic[i] = 0
for i in range(len(classes)):
    tail = classes[i][0]
    dic[tail] += 1
from queue import Queue
q = Queue()
res = []
for i in range(len(dic)):
    if dic[i] == 0:
        q.put(i)
while q.qsize() != 0:
    node = q.get()
    res.append(node)
    for j in range(len(classes)):
        if classes[j][1] == node:
            tail2 = classes[j][0]
            dic[tail2] -= 1
            if dic[tail2] == 0:
                q.put(tail2)
if len(res) == num:
    print(res)
else:
    print("[]")
