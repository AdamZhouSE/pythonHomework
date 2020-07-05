def check(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True


def get(st):
    count = 0
    for i in range(len(st)):
        for j in range(len(st)):
            s = st[i][1]+st[j][1]
            if check(s):
                count += 1
    return count
            

num = int(input())
st = []
for i in range(num):
    s = input().split(" ")
    s[0] = int(s[0])
    st.append(s)
print(get(st))