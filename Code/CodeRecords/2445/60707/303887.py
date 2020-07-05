
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if s is None or t is None:
        return "false"
    if s == "" and t == "":
        return "true"
    if len(s) != len(t):
        return "false"
    sett = set(t)
    for m in sett:
        if s.count(m) != t.count(m):
            return "false"
    return "true"


inp = input().split("\"")
s = inp[1]
t = inp[3]
print(isAnagram(s, t))
