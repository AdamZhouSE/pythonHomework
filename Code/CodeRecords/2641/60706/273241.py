import collections
s1=input()
s2=input()
count_dict = collections.Counter(s1)
m = len(s1)
i = 0
j = m - 1
ans='False'
while j < len(s2):
    if collections.Counter(s2[i:j+1]) == count_dict:
        ans='True'
    i += 1
    j += 1
print(ans)