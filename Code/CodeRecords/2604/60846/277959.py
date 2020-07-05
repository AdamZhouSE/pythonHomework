import bisect
def nextGreatestLetter( letters, target):
    index = bisect.bisect(letters, target)
    return letters[index % len(letters)]
print(nextGreatestLetter(eval(input()),input()))
