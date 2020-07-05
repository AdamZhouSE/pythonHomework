move = int(input())
rawString = input()
alphabet1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet2 = alphabet1.copy()
for i in range(move):
    alphabet2.append(alphabet2.pop(0))
string = ""
for letter in rawString:
    string = string + alphabet2[alphabet1.index(letter)]
print(string,end="")