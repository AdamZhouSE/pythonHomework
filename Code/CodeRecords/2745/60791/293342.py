from collections import defaultdict
def ladderLength( begin: str, end: str, words: list) -> int:

	L = len(begin)
	all_combo_dict = defaultdict(list)
	for word in words:
		for i in range(L):
			all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

	q,visited = [(begin,1)],set()
	while(q):
		word, step = q.pop(0)
		if word not in visited:
			print(word,step)
			visited.add(word)
			if word == end:
				print(q)
				return step
			for i in range(len(word)):
				tmp = word[:i] + '*' + word[i+1:]
				for neigh in all_combo_dict[tmp]:
					q.append((neigh,step+1))
	return 0
begin = input()
end = input()
l = eval(input())
pro = []
for i in range(len(end)+1):
    pro.append([])

for i in range(len(l)):
    index = 0
    for j in range(len(l[i])):
        if l[i][j] == end[j]:
            index += 1
    pro[index].append(l[i])
print([])