class Solution:
	def wordJoint(self, s: str, words: [str]):
		cover = [i for i in range(0, len(s))]
		
		for word in words:
			index = s.find(word)
			while index != -1:
				cover[index] = max(cover[index], index + len(word))
				index = s.find(word,index + 1)
		
		start, end = 0, cover[0]
		count = 1
		while start != end:
			if end == len(s):
				return count
			temp = max(cover[i] for i in range(start + 1, end + 1))
			start = end
			end = temp
			count += 1
		
		return -1
	
	
if __name__ == '__main__':
	n = int(input())
	s = input()
	words = []
	while n > 0:
		n -= 1
		words.append(input())
	x = Solution()
	print(x.wordJoint(s,words))