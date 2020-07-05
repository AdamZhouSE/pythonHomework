class Solution:
	def binaryAdd(self,src,dest):
		src = list(src)
		src.reverse()
		s = len(src)
		dest = list(dest)
		dest.reverse()
		d = len(dest)
		
		CF = 0
		for i in range(0,max(s,d)):
			ceilS = ceilD = 0
			if i < s:
				ceilS = int(src[i])
			if i < d:
				ceilD = int(dest[i])
			sum = CF + ceilD + ceilS
			CF = sum // 2
			sum = sum % 2
			if i < s:
				src[i] = str(sum)
			else:
				src.append(str(sum))
		if CF:
			src.append("1")
		src.reverse()
		return "".join(src)
	
if __name__ == '__main__':
    x = Solution()
    print(x.binaryAdd(input(),input()))