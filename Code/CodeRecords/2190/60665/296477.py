class Solution:
	
	def sort(self, sa, rank, tp, n, m):
		tax = [0] * m
		for i in range(n):
			tax[rank[i]] += 1
		for i in range(1, m):
			tax[i] += tax[i-1]
		for i in range(n-1,-1,-1):
			sa[tax[rank[tp[i]]]-1] = tp[i]
			tax[rank[tp[i]]] -= 1  # 第一关键字相等， 第二关键字排在后面的排名减一
			
	def cmp(self, tp, la, lb, w):
		if tp[la] == tp[lb]:
			if la + w >= len(tp) and lb + w >= len(tp):
				return True
			elif la + w >= len(tp) or lb + w >= len(tp):
				return False
			elif tp[la+w] == tp[lb+w]:
				return True
		return False
	
	def suffix(self, s):
		n = len(s)
		rank = [ord(i) for i in s]  # 第一关键字
		tp = [i for i in range(n)]  # 第二关键字
		sa = [0] * n
		m = 127
		
		# 以单字符为第一关键字排序初始化sa， 未引入第二关键字
		self.sort(sa, rank, tp, n, m)
		
		w = p = 1
		# 当排名数（从0开始）等于数组长度时退出
		while p < n-1:
			p = 0
			# 第二关键字越界的设为最小，排在tp数组最前
			for i in range(n-w,n):
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
				if not self.cmp(tp, sa[i], sa[i-1], w):
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
	
	def MrBen(self, s, k):
		n = len(s)
		res = [0] * (n + 1)
		length = [1] * (n + 1)
		sa, height = self.suffix(s)
		if k == 1:
			start = height[1] + 1
			for j in range(start, n-sa[0]):
				res[j] += 1
			for i in range(1, n):
				start = height[i] + 1
				for j in range(start, n - sa[i]):
					res[j] += 1
		else:
			for i in range(1, n):
				for j in range(1, height[i] + 1):
					length[j] += 1
				if height[i] < height[i - 1]:
					for j in range(height[i] + 1, height[i - 1] + 1):
						if length[j] == k:
							res[j] += 1
						length[j] = 1
			for j in range(1,height[n-1]+1):
				if length[j] == k:
					res[j] += 1
					length[j] = 1
		
		maxTimes = 0
		length = 0
		for i in range(1,n+1):
			if res[i] >= maxTimes:
				length = i
				maxTimes = res[i]
		
		if maxTimes == 0:
			return -1
		else:
			return length
		
		
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		info = input().split()
		print(x.MrBen(info[0], int(info[1])))