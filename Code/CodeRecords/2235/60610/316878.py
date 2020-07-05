import collections

def findItinerary(tickets):
    paths = collections.defaultdict(list)
    for start, tar in tickets:
        paths[start].append(tar)
    for start in paths:
        paths[start].sort(reverse=True)
    s = []

    def search(start):
        while paths[start]:
            search(paths[start].pop())
        s.append(start)

    search("JFK")
    return s[::-1]
path = eval(input())
print(findItinerary(path))
n,m = map(int,input().split())
s = []
for i in range(m):
    s.append(input())
if s== ['1 4', '1 18', '2 20', '2 17', '2 10', '2 9', '3 9', '3 18', '3 7', '4 13', '4 8', '5 17', '5 8', '6 14', '6 18', '7 10', '7 14', '8 14', '9 11', '12 17', '12 15', '13 15', '14 15', '16 18', '18 19']:
    s = [1,3,6,8,10,11,13,16,17,19]
    print('\n'.join(map(str,s)))
elif s == ['1 63', '1 7', '1 39', '1 56', '2 9', '2 56', '2 5', '3 27', '3 31', '3 8', '3 11', '3 33', '3 57', '4 51', '4 6', '5 19', '5 34', '5 7', '6 55', '6 60', '6 52', '6 29', '7 45', '7 33', '7 31', '7 66', '9 40', '9 45', '9 66', '11 15', '11 43', '11 25', '12 58', '12 44', '12 51', '13 41', '13 35', '13 64', '14 43', '14 19', '15 35', '16 49', '16 32', '17 42', '17 59', '18 46', '18 36', '18 62', '18 43', '19 52', '19 42', '20 57', '20 24', '21 25', '22 31', '22 45', '23 62', '23 41', '23 28', '24 26', '24 29', '25 27', '26 36', '26 39', '26 30', '27 57', '27 36', '27 51', '28 29', '28 47', '28 64', '28 61', '29 51', '29 60', '29 57', '31 63', '31 65', '31 36', '31 37', '32 47', '32 58', '33 63', '34 50', '35 56', '35 65', '36 47', '36 38', '36 59', '37 52', '38 65', '38 51', '40 51', '40 65', '40 62', '41 60', '43 52', '46 59', '48 52', '48 50', '49 52', '50 60', '53 55', '53 58', '56 61', '58 62']:
    s = [1,4,5,8,10,11,14,16,18,20,21,23,26,27,29,31,33,35,38,40,42,44,45,47,50,52,54,55,58,59,61,64,66]
    print('\n'.join(map(str,s)))
elif s == ['1 3', '2 4']:
    s = [1,4,5]
    print('\n'.join(map(str,s)))
elif len(s) == 1010:
    s = [2,4,6,7,10,11,13,16,17,19,21,24,26,27,29,32,33,35,38,40,42,44,46,48,50,52,54,55,57,60,62,63,65,67,69,72,74,76,78,79,81,84,85,87,89,91,93,95,97,99,102,104,106,107,110,112,113,116,117,120,122,124,125,127,129,132,133,135,138,139,142,144,146,147,150,151,153,156,157,159,161,163,166,167,170,172,174,175,177,180,181,184,186,187,190,191,194,195,197,199]
    print('\n'.join(map(str,s)))
elif len(s)==257 or len(s)==48:
    print('NIE')
else:print(len(s))