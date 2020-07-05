s = input()
suffix = []
suffixIndex = []

for i in range(len(s)):
    suffix.append(s[i:])
    suffixIndex.append(i + 1)

for index in range(len(suffix) - 1):
    if len(suffix[index]) > len(suffix[index + 1]):
        temp = suffix[index + 1]
        suffix[index + 1] = suffix[index]
        suffix[index] = temp

        temp1 = suffixIndex[index + 1]
        suffixIndex[index + 1] = suffixIndex[index]
        suffixIndex[index] = temp1

    elif ord(suffix[index][0]) > ord(suffix[index + 1][0]):
        temp = suffix[index + 1]
        suffix[index + 1] = suffix[index]
        suffix[index] = temp

        temp1 = suffixIndex[index + 1]
        suffixIndex[index + 1] = suffixIndex[index]
        suffixIndex[index] = temp1

for num in suffixIndex:
    print(num, end=' ')