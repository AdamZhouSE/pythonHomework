class Solution:
	def monogram(self,word1,word2):
		if len(word1) != len(word2):
			return "false"
		
		alph = {}
		for ele in word1:
			if ele not in alph:
				alph[ele] = 1
			else:
				alph[ele] = alph[ele] + 1
		for ele in word2:
			if ele not in alph:
				return "false"
			else:
				if alph[ele] == 1:
					alph.pop(ele)
				else:
					alph[ele] = alph[ele] - 1
		
		return "true"
	

if __name__ == '__main__':
    x = Solution()
    s = input().split('"');
    print(x.monogram(s[1],s[3]))