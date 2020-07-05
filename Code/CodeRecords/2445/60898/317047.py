def fun(s,t):
    bool = True
    matrix_s = [0 for i in range(26)]
    for i in range(len(s)):
        num = int(ord(s[i]) - 97)
        matrix_s[num]+=1
    for i in range(len(t)):
        num = int(ord(t[i]) - 97)
        matrix_s[num]-=1
    for i in range(26):
        if matrix_s[i] != 0:
            print("false")
            bool = False
            break
    if bool:
        print("true")

n = input()
li = n.replace(" ","").split(",")
exec(li[0]); exec(li[1])
fun(s,t)

def Solution(nums,target):
    try:
        index = nums.index(target)
    except:
        return -1
    return index

n = input()
m = input()
nums = n.split(",")
target = m

print(Solution(nums,target))