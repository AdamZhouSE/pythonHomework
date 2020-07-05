import sys

class union_find:
	def __init__(self, size):
		self.p = [i for i in range(size + 1)]
		self.sz = [1] * (size + 1)

	def find(self, x):
		# print(self.p)
		while (x != self.p[x]):
			# print('%d, now father: %d' % (x, self.p[x]))
			x = self.p[self.p[x]]
		return x

	def union(self, x, y):
		p1 = self.find(x)
		p2 = self.find(y)
		if self.sz[p1] > self.sz[p2]:
			self.p[p2] = p1
			self.sz[p1] += self.sz[p2]
		else:
			self.p[p1] = p2
			self.sz[p2] += self.sz[p1]

	def connected(self, x, y):
		return self.find(x) == self.find(y)

e = []
n, m = map(int, input().split())
for line in sys.stdin.readlines():
	e.append(tuple(map(int, line.split())))
e.sort(key=lambda x: x[2])
# print(e)
ans = 0
uni = union_find(n)
count = 0
for u, v, w in e:
	if not uni.connected(u, v):
		uni.union(u, v)
		ans += w
		count += 1
	if count == n - 1:
		break
print(ans,end='')