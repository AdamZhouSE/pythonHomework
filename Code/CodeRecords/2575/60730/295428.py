seq = list(input())
if seq == "":
    print("[]")
heap = []
ans = []
tmp = 0
for i in range(len(seq)):
    if seq[i] == "(":
        heap.append(tmp)
        ans.append(tmp)
        tmp += 1
    if seq[i] == ")":
        ans.append(heap[len(heap)-1])
        heap = heap[:-1]
        tmp -= 1
print(ans)
