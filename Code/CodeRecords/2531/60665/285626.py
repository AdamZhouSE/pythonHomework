class Solution:
	def frequencySort(self, s):
		table = {}
		for letter in s:
			table[letter] = table.get(letter, 0) + 1
		
		res = ''
		for key in sorted(table.keys(), key=lambda x:table[x], reverse=True):
			res += key*table[key]
		return res
	
if __name__ == '__main__':
	x =Solution()
	print(x.frequencySort(input()))