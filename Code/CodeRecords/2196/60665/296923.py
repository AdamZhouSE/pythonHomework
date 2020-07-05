class Solution:
	
	def sort(self, sa, rank, tp, n, m):
		tax = [0] * m
		for i in range(n):
			tax[rank[i]] += 1
		for i in range(1, m):
			tax[i] += tax[i - 1]
		for i in range(n - 1, -1, -1):
			sa[tax[rank[tp[i]]] - 1] = tp[i]
			tax[rank[tp[i]]] -= 1  # 第一关键字相等， 第二关键字排在后面的排名减一
	
	def cmp(self, tp, la, lb, w):
		if tp[la] == tp[lb]:
			if la + w >= len(tp) and lb + w >= len(tp):
				return True
			elif la + w >= len(tp) or lb + w >= len(tp):
				return False
			elif tp[la + w] == tp[lb + w]:
				return True
		return False
	
	def suffix(self, s):
		n = len(s)
		rank = [ord(i) for i in s]  # 第一关键字
		tp = [i for i in range(n)]  # 第二关键字
		sa = [0] * n
		m = 16000
		
		# 以单字符为第一关键字排序初始化sa， 未引入第二关键字
		self.sort(sa, rank, tp, n, m)
		
		w = p = 1
		# 当排名数（从0开始）等于数组长度时退出
		while p < n - 1:
			p = 0
			# 第二关键字越界的设为最小，排在tp数组最前
			for i in range(n - w, n):
				tp[p] = i
				p += 1
			# 由上一次的sa得到对应的第二关键字的排序
			for i in range(n):
				if sa[i] >= w:
					tp[p] = sa[i] - w
					p += 1
			# 引入第二关键字排序更新sa，tp暂存上一轮的rank用于cmp比较
			self.sort(sa, rank, tp, n, m)
			temp = tp
			tp = rank
			rank = temp
			
			# 由sa得到互逆的rank，并将相等的字符串排名设为相同
			rank[sa[0]] = 0
			p = 0
			for i in range(1, n):
				if not self.cmp(tp, sa[i], sa[i - 1], w):
					p += 1
				rank[sa[i]] = p
			
			# m更新为排名数，w翻倍
			m = p + 1
			w *= 2
		
		# 由公式，lcp(1,k) = min(lcp(i,j),lcp(j,k))对任一位于i，k之间的j
		# 由公式，Height[rank[i]] >= Height[rank[i-1]] - 1
		Height = [0] * n
		k = j = 0
		for i in range(0, n):
			if rank[i] == 0:
				Height[rank[i]] = 0
				continue
			j = sa[rank[i] - 1]
			k = max(k - 1, 0)
			while i + k < n and j + k < n and s[i + k] == s[j + k]:
				k += 1
			Height[rank[i]] = k
		return sa, Height
	
	def subMatrix(self, matrix, n, m):
		res = 0
		for i in range(m):
			table = {}
			top, bot = 15000, 0
			s = ''
			for k in range(m - i):
				for j in range(n):
					if Matrix[j][k: k + i + 1] not in table:
						top -= 1
						table[Matrix[j][k: k + i + 1]] = chr(top)
					s += table[Matrix[j][k: k + i + 1]]
				s += chr(bot)
				bot += 1
			
			sa, height = self.suffix(s)
			# 取余并用行数减去（lcp <= n）得到当前后缀长度，进一步算相异字串个数
			# 长度为零即遇到分隔字符，跳出
			res += n - sa[len(height)-1]%(n+1)
			for i in range(len(height)-1,0,-1):
				length = n - sa[i-1]%(n+1)
				res += length - height[i]
		return res
	
if __name__ == '__main__':
	x = Solution()
	data = [int(i) for i in input().split()]
	Matrix = []
	for i in range(data[0]):
		Matrix.append(input())
	print(x.subMatrix(Matrix, data[0], data[1]),end="")