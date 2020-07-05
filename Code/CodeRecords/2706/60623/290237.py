import collections


class UF:
	def __init__(self):
		self.parent = {}

	def find(self, x):
		self.parent.setdefault(x, x)
		while x != self.parent[x]:
			x = self.parent[x]
		return x

	def union(self, p, q):
		self.parent[self.find(p)] = self.find(q)

accounts = eval(input())
uf = UF()
email_to_name = {}
res = collections.defaultdict(list)
for account in accounts:
	for i in range(1, len(account)):
		email_to_name[account[i]] = account[0]
		if i < len(account) - 1: uf.union(account[i], account[i + 1])
for email in email_to_name:
	res[uf.find(email)].append(email)
print([[email_to_name[value[0]]] + value for value in res.values()])