# Python 3 implementation to find the 
# uncommon characters of the two strings 

# size of the hash table 
MAX_CHAR = 26

# function to find the uncommon characters 
# of the two strings 
def findAndPrintUncommonChars(str1, str2): 
	
	# mark presence of each character as 0 
	# in the hash table 'present[]' 
	present = [0] * MAX_CHAR 
	for i in range(0, MAX_CHAR): 
		present[i] = 0

	l1 = len(str1) 
	l2 = len(str2) 
	
	# for each character of str1, mark its 
	# presence as 1 in 'present[]' 
	for i in range(0, l1): 
		present[ord(str1[i]) - ord('a')] = 1
		
	# for each character of str2 
	for i in range(0, l2): 
		
		# if a character of str2 is also present 
		# in str1, then mark its presence as -1 
		if(present[ord(str2[i]) - ord('a')] == 1 or
		present[ord(str2[i]) - ord('a')] == -1): 
			present[ord(str2[i]) - ord('a')] = -1

		# else mark its presence as 2 
		else: 
			present[ord(str2[i]) - ord('a')] = 2

	# print all the uncommon characters 
	for i in range(0, MAX_CHAR): 
		if(present[i] == 1 or present[i] == 2): 
			print(chr(i + ord('a')), end = " ") 

# Driver Code 
if __name__ == "__main__": 
	str1 = input()
	str2 = input()
	findAndPrintUncommonChars(str1, str2) 


