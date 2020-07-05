class Solution:
	def classfiy(self, words):
		classTable = {}
		for word in words:
			table = {}
			for letter in word:
				table[letter] = table.get(letter, 0) + 1
			word = ""
			for key in sorted(table.keys()):
				word += (key + "{:d}".format(table[key]))
			classTable[word] = classTable.get(word, 0) + 1
		
		return len(classTable.keys())
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	words = []
	while n > 0:
		n -= 1
		words.append(input())
	print(x.classfiy(words),end="")