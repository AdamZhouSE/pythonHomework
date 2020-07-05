
def selection_sort(dic, arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            if dic[arr[j]] < dic[arr[minimum]]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


s = input()
t = input()
temp = "qwertyuiopasdfghjklzxcvbnm"
dic = dict()
t = list(t)
s = list(s)
for i in list(temp):
    dic[i] = -1
for i in range(len(s)):
    dic[s[i]] = i

t = selection_sort(dic, t)
print("".join(t))