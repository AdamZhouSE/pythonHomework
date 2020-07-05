
def minusDiv(a) -> [int, int]:
    if a % -2 == 0:
        return [a // -2, 0]
    return [a//-2 + 1, a%-2+2]

arr1 = list(eval("["+input()+"]"))
arr2 = list(eval("["+input()+"]"))
arr1.reverse()
arr2.reverse()
val1 = 0
val2 = 0
div = 1
for i in arr1:
    val1 += i*div
    div *= -2
div = 1
for i in arr2:
    val2 += i*div
    div *= -2

res = val2+val1
out = []
while res != 0:
    t = minusDiv(res)
    res = t[0]
    out.append(t[1])
out.reverse()
print(out)
