initial = input()

j = len(initial) - 1
isPalindrome = True
for i in range(0, j):
    if initial[i] != initial[j]:
        isPalindrome = False
        break
    j -= 1
    if i>j:
        break
print(isPalindrome)
