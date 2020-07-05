def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums_str1 = nums_str.replace('\"', '')

    nums = [str(n) for n in nums_str1.split(",")];
    return nums;

def isValid(word1, word2):
    for i in range (len(word1)):
        if word1[i] in word2:
            return False
    return True

def maxProduct(words):

    maxLength = 0
    for i in range (len(words)):
        for j in range (i + 1, len(words)):
            if isValid(words[i], words[j]):
                maxLength = max(maxLength, len(words[i]) * len(words[j]))
    return maxLength




l = getInput()

print(maxProduct(l))