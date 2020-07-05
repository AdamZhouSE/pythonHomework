class Solution:
	def smallestStringWithSwaps(self, s: str, pairs: [[int]]) -> str:
		unions = []
		delete = []
		for pair in pairs:
			contain = -1
			for i in range(0,len(unions)):
				if not delete[i]:
					if pair[0] in unions[i] or pair[1] in unions[i]:
						if contain != -1:
							unions[contain] = unions[contain].union(unions[i])
							delete[i] = True
						else:
							unions[i].add(pair[0])
							unions[i].add(pair[1])
							contain = i
			if contain == -1:
				unions.append(set(pair))
				delete.append(False)
		
		res = [""]*len(s)
		for k in range(0,len(unions)):
			if not delete[k]:
				union = list(unions[k])
				union.sort()
				part = [""] * len(union)
				for i in range(0,len(union)):
					part[i] = s[union[i]]
				part.sort()
				for i in range(0,len(union)):
					res[union[i]] = part[i]
		
		for i in range(0,len(s)):
			if res[i] == "":
				res[i] = s[i]
		
		return "".join(res)
		

if __name__ == '__main__':
	x = Solution()
	print(x.smallestStringWithSwaps(input(),eval(input())))