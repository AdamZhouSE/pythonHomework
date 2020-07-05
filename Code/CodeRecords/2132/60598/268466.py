string = input()

# zero one two three four five six seven eight nine
count = [0 for x in range(26)]
nums = [0 for i in range(10)]
for i in range(len(string)):
    count[ord(string[i])-ord('a')] += 1
#6
if count[ord("x")-ord("a")] != 0:
    nums[6] += count[ord("x")-ord("a")]
    count[ord("s") - ord("a")] -= count[ord("x")-ord("a")]
    count[ord("i") - ord("a")] -= count[ord("x")-ord("a")]
    count[ord("x") - ord("a")] -= count[ord("x")-ord("a")]
#7
if count[ord("s")-ord("a")] != 0:
    nums[7] = count[ord("s")-ord("a")]
    count[ord("v")-ord("a")] -= count[ord("s")-ord("a")]
    count[ord("n")-ord("a")] -= count[ord("s")-ord("a")]
    count[ord("e")-ord("a")] -= 2 * count[ord("s")-ord("a")]
    count[ord("s")-ord("a")] -= count[ord("s")-ord("a")]
#5
if count[ord("v")-ord("a")] != 0:
    nums[5] = count[ord("v")-ord("a")]
    count[ord("f")-ord("a")] -= count[ord("v")-ord("a")]
    count[ord("i")-ord("a")] -= count[ord("v")-ord("a")]
    count[ord("e")-ord("a")] -= count[ord("v")-ord("a")]
    count[ord("v")-ord("a")] -= count[ord("v")-ord("a")]
#0
if count[ord("z")-ord("a")] != 0:
    nums[0] += count[ord("z")-ord("a")]
    count[ord("r")-ord("a")] -= count[ord("z")-ord("a")]
    count[ord("o")-ord("a")] -= count[ord("z")-ord("a")]
    count[ord("e")-ord("a")] -= count[ord("z")-ord("a")]
    count[ord("z")-ord("a")] -= count[ord("z")-ord("a")]
#4
if count[ord("f")-ord("a")] != 0:
    nums[4] += count[ord("f")-ord("a")]
    count[ord("r") - ord("a")] -= count[ord("f")-ord("a")]
    count[ord("o") - ord("a")] -= count[ord("f")-ord("a")]
    count[ord("u") - ord("a")] -= count[ord("f")-ord("a")]
    count[ord("f") - ord("a")] -= count[ord("f") - ord("a")]
#3
if count[ord("r") - ord("a")] != 0:
    nums[3] += count[ord("r")-ord("a")]
    count[ord("h")-ord("a")] -= count[ord("r")-ord("a")]
    count[ord("e")-ord("a")] -= count[ord("r")-ord("a")]
    count[ord("t")-ord("a")] -= count[ord("r")-ord("a")]
    count[ord("r") - ord("a")] -= count[ord("r") - ord("a")]
#8
if count[ord("h")-ord("a")] != 0:
    nums[8] += count[ord("h")-ord("a")]
    count[ord("t") - ord("a")] -= count[ord("h") - ord("a")]
    count[ord("e") - ord("a")] -= count[ord("h") - ord("a")]
    count[ord("i") - ord("a")] -= count[ord("h") - ord("a")]
    count[ord("g") - ord("a")] -= count[ord("h") - ord("a")]
    count[ord("h") - ord("a")] -= count[ord("h") - ord("a")]

#2
if count[ord("t")-ord("a")] != 0:
    nums[2] += count[ord("t")-ord("a")]
    count[ord("o")-ord("a")] -= count[ord("t")-ord("a")]
    count[ord("w")-ord("a")] -= count[ord("t")-ord("a")]
    count[ord("t")-ord("a")] -= count[ord("t")-ord("a")]
#1
if count[ord("o")-ord("a")] != 0:
    nums[1] += count[ord("o")-ord("a")]
    count[ord("n")-ord("a")] -= count[ord("o")-ord("a")]
    count[ord("e")-ord("a")] -= count[ord("o")-ord("a")]
    count[ord("o")-ord("a")] -= count[ord("o")-ord("a")]
#9
if count[ord("n")-ord("a")] != 0:
    nums[9] += count[ord("n")-ord("a")]*2
result = ""
for j in range(len(nums)):
    result += str(j)*nums[j]
print(result)
