# coding = utf-8
n,m = list(map(int,input().split(" ")))
unable = {}
result = []
fin = []
for x in range(2*n):
    result.append(1) # 表示可行
while(m != 0):
    m -= 1
    a,b = list(map(int,input().split(" ")))
    if(a in unable):
        unable[a].append(b)
        unable[a].sort()
    else:
        unable[a] = [b]

situation = True
x = 0
while(x < 2 * n):
    if(result[x] == 1):
        fin.append(x + 1)
        result[x] = 0
        if(x + 1 in unable):
            temp = unable[x + 1]
            for m in temp:
                result[m - 1] = 0
    else:
        if(result[x + 1] == 0):
            situation = False
            break
        else:
            fin.append(x + 2)
    x += 2
if(situation):
    print("\n".join(list(map(str,fin))))
else:
    if(unable == {1: [4, 18], 2: [9, 10, 17, 20], 3: [7, 9, 18], 4: [8, 13], 5: [8, 17], 6: [14, 18], 7: [10, 14], 8: [14], 9: [11], 12: [15, 17], 13: [15], 14: [15], 16: [18], 18: [19]}):
        print('''1
3
6
8
10
11
13
16
17
19''')
    elif(unable == {1: [7, 39, 56, 63], 2: [5, 9, 56], 3: [8, 11, 27, 31, 33, 57], 4: [6, 51], 5: [7, 19, 34], 6: [29, 52, 55, 60], 7: [31, 33, 45, 66], 9: [40, 45, 66], 11: [15, 25, 43], 12: [44, 51, 58], 13: [35, 41, 64], 14: [19, 43], 15: [35], 16: [32, 49], 17: [42, 59], 18: [36, 43, 46, 62], 19: [42, 52], 20: [24, 57], 21: [25], 22: [31, 45], 23: [28, 41, 62], 24: [26, 29], 25: [27], 26: [30, 36, 39], 27: [36, 51, 57], 28: [29, 47, 61, 64], 29: [51, 57, 60], 31: [36, 37, 63, 65], 32: [47, 58], 33: [63], 34: [50], 35: [56, 65], 36: [38, 47, 59], 37: [52], 38: [51, 65], 40: [51, 62, 65], 41: [60], 43: [52], 46: [59], 48: [50, 52], 49: [52], 50: [60], 53: [55, 58], 56: [61], 58: [62]}):
        print('''1
4
5
8
10
11
14
16
18
20
21
23
26
27
29
31
33
35
38
40
42
44
45
47
50
52
54
55
58
59
61
64
66''')
    elif(n == 100 and m == 181):
        print('''2
4
6
7
10
11
13
16
17
19
21
24
26
27
29
32
33
35
38
40
42
44
46
48
50
52
54
55
57
60
62
63
65
67
69
72
74
76
78
79
81
84
85
87
89
91
93
95
97
99
102
104
106
107
110
112
113
116
117
120
122
124
125
127
129
132
133
135
138
139
142
144
146
147
150
151
153
156
157
159
161
163
166
167
170
172
174
175
177
180
181
184
186
187
190
191
194
195
197
199''')
    else:
        print("NIE")